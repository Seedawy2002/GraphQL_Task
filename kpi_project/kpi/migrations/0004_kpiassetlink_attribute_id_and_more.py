# Generated by Django 5.1.2 on 2024-11-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0003_kpiinfo_kpiassetlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpiassetlink',
            name='attribute_id',
            field=models.CharField(default='default_attribute', max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='kpiassetlink',
            unique_together={('asset_id', 'attribute_id')},
        ),
    ]
