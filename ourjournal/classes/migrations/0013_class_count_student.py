# Generated by Django 4.0.6 on 2024-03-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_alter_shedule_class_user_alter_shedule_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='count_student',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
