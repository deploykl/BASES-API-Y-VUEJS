# Generated by Django 5.0.14 on 2025-07-27 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_user_modulos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modulo',
            old_name='name',
            new_name='codename',
        ),
    ]
