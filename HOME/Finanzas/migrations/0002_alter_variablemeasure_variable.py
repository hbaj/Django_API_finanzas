# Generated by Django 3.2.7 on 2021-10-26 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finanzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variablemeasure',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variableMeasures', to='Finanzas.variable'),
        ),
    ]
