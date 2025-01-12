import graphene
from graphene_django.types import DjangoObjectType
from .models import KPIInfo

# GraphQL Types
class KPIInfoType(DjangoObjectType):
    class Meta:
        model = KPIInfo
        fields = "__all__"

# Mutations
class CreateKPI(graphene.Mutation):
    kpi = graphene.Field(KPIInfoType)

    class Arguments:
        name = graphene.String(required=True)
        expression = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, name, expression, description=None):
        kpi = KPIInfo.objects.create(name=name, expression=expression, description=description)
        return CreateKPI(kpi=kpi)

class UpdateKPI(graphene.Mutation):
    kpi = graphene.Field(KPIInfoType)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        expression = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name=None, expression=None, description=None):
        try:
            kpi = KPIInfo.objects.get(id=id)
            if name:
                kpi.name = name
            if expression:
                kpi.expression = expression
            if description:
                kpi.description = description
            kpi.save()
            return UpdateKPI(kpi=kpi)
        except KPIInfo.DoesNotExist:
            raise Exception("KPI with the given ID does not exist.")

class DeleteKPI(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        try:
            kpi = KPIInfo.objects.get(id=id)
            kpi.delete()
            return DeleteKPI(success=True)
        except KPIInfo.DoesNotExist:
            raise Exception("KPI with the given ID does not exist.")

# Queries
class Query(graphene.ObjectType):
    # Define an empty query or add a simple placeholder query
    all_kpis = graphene.List(KPIInfoType)

    def resolve_all_kpis(self, info):
        return KPIInfo.objects.all()

# Root Schema
class Mutation(graphene.ObjectType):
    create_kpi = CreateKPI.Field()
    update_kpi = UpdateKPI.Field()
    delete_kpi = DeleteKPI.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
