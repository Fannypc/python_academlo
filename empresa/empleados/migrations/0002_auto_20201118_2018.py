# Generated by Django 2.2.14 on 2020-11-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='managers',
            field=models.ManyToManyField(related_name='empleados', to='managers.Manager'),
        ),
    ]