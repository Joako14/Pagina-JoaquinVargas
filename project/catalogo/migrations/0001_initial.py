# Generated by Django 4.2.5 on 2023-10-12 23:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AñoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
            ],
            options={
                'verbose_name': 'año',
                'verbose_name_plural': 'año',
            },
        ),
        migrations.CreateModel(
            name='BateriaCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bateria', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('tipo_bateria', models.CharField(max_length=100)),
                ('positivo', models.CharField(max_length=100)),
                ('amperaje', models.CharField(max_length=100)),
                ('potencia_arranque', models.CharField(max_length=100)),
                ('tipo_borne', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripcion')),
            ],
            options={
                'verbose_name': 'bateria',
                'verbose_name_plural': 'bateria',
            },
        ),
        migrations.CreateModel(
            name='MarcaCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marca',
            },
        ),
        migrations.CreateModel(
            name='ModeloCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelo',
            },
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripcion')),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='fecha de actualizacion')),
                ('año', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.añocategoria', verbose_name='año')),
                ('bateria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.bateriacategoria', verbose_name='bateria')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.marcacategoria', verbose_name='marca')),
                ('modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.modelocategoria', verbose_name='modelo')),
            ],
            options={
                'verbose_name': 'catalogo',
                'verbose_name_plural': 'catalogo',
            },
        ),
    ]
