# Generated by Django 2.2.14 on 2020-11-18 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0002_auto_20201112_2123'),
        ('editoriales', '0002_auto_20201111_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('paginas', models.IntegerField()),
                ('autores', models.ManyToManyField(related_name='autores', to='autores.Autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editoriales.Editorial')),
            ],
        ),
    ]
