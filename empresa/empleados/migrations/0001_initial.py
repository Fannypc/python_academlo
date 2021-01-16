# Generated by Django 2.2.14 on 2020-11-19 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managers', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areas.Area')),
                ('managers', models.ManyToManyField(related_name='empleado', to='managers.Manager')),
            ],
        ),
    ]