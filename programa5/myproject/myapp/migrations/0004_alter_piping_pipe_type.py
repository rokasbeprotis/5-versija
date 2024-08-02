# Generated by Django 5.0.6 on 2024-07-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_compressor_discharge_conn_compressor_oil_conn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piping',
            name='pipe_type',
            field=models.CharField(choices=[('discharge', 'Discharge Line'), ('liquid', 'Liquid Line'), ('condensing', 'Condensing Line'), ('suction', 'Suction Line'), ('oil', 'Oil Line')], max_length=20),
        ),
    ]