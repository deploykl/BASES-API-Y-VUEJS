# Generated by Django 5.0.14 on 2025-07-24 20:57

import api.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='user',
            name='departamento',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='user',
            name='distrito',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Distrito'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='img/empty.png', null=True, upload_to=api.user.models.user_image_path),
        ),
    ]
