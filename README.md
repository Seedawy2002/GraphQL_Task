## What's New
### Key Features
- **GraphQL API Integration**:
   - **Mutations for KPI Management**:
     - **CreateKPI**: Add a new KPI.
     - **UpdateKPI**: Modify an existing KPI.
     - **DeleteKPI**: Remove a KPI.
   - **Queries for Data Retrieval**:
     - **allKpis**: Fetch all KPIs in the system.
---

## Steps Followed
1. **Installed Graphene-Django**:
   ```bash
   pip install graphene-django
   ```

2. **Configured GraphQL in Django**:
   - Added `graphene_django` to `INSTALLED_APPS` in `settings.py`:
     
     ```python
     INSTALLED_APPS += ['graphene_django']
     ```
     
   - Configured the schema:
     ```python
     GRAPHENE = {
         "SCHEMA": "kpi.schema.schema"  # Path to your schema
     }
     ```
   - Added the GraphQL endpoint to `urls.py`:
     ```python
     from graphene_django.views import GraphQLView

     urlpatterns += [
         path("graphql/", GraphQLView.as_view(graphiql=True)),  # GraphQL endpoint
     ]
     ```

3. **Added `schema.py`**:
   - Implemented the necessary queries and mutations in the `kpi_project/kpi/schema.py` file.

4. **Started the Django Server**:
   ```bash
   python manage.py runserver --noreload
   ```
   Accessed the server at: [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/)

5. **Executed GraphQL Queries**:
   - Performed various queries and mutations as described below.

---

## GraphQL API Documentation

### Queries Performed
#### 1. **List All KPIs**
Retrieve all KPIs in the database, including their ID, name, expression, and description:
```graphql
{
  allKpis {
    id
    name
    expression
    description
  }
}
```

---

#### 2. **Create a KPI**
Add a new KPI to the system:
```graphql
mutation {
  createKpi(name: "Revenue KPI", expression: "value * 0.1", description: "Calculates 10% of value") {
    kpi {
      id
      name
      expression
      description
    }
  }
}
```

---

#### 3. **Update an Existing KPI**
Modify the details of an existing KPI:
```graphql
mutation {
  updateKpi(id: 1, name: "Updated KPI Name", expression: "value + 10", description: "Updated description") {
    kpi {
      id
      name
      expression
      description
    }
  }
}
```

---

#### 4. **Delete a KPI**
Remove a KPI from the database:
```graphql
mutation {
  deleteKpi(id: 1) {
    success
  }
}
```

---

## Testing

To demonstrate the functionality of the new GraphQL API, you can watch the following video:

[**Watch the Testing Demo Video**](https://drive.google.com/file/d/1WbtZIz-UwTUUl2ip6QcpAr3xA55jokC7/view?usp=sharing)
