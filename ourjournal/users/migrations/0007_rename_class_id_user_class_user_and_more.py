# Generated by Django 5.0.2 on 2024-03-14 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Class_id',
            new_name='class_user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='status_id',
            new_name='status',
        ),
    ]