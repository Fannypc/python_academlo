# Generated by Django 2.2.14 on 2020-11-23 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('creditos', models.IntegerField()),
                ('descripcion', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
