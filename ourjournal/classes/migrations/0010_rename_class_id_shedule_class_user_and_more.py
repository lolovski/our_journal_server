# Generated by Django 5.0.2 on 2024-03-14 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_alter_class_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shedule',
            old_name='class_id',
            new_name='class_user',
        ),
        migrations.RenameField(
            model_name='shedule',
            old_name='day_id',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='shedule',
            old_name='lesson_id',
            new_name='lesson',
        ),
    ]