# Generated by Django 5.0.2 on 2024-03-14 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listUsers', '0004_validuser_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validuser',
            old_name='class_id',
            new_name='class_user',
        ),
    ]
