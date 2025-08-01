# Generated by Django 5.0.14 on 2025-07-27 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redes', to='gore.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('red', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitales', to='gore.red')),
            ],
        ),
    ]
