# Generated by Django 5.0.14 on 2025-07-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_options_user_created_by_user_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=False, verbose_name='En línea'),
        ),
    ]
