# Generated by Django 5.0.2 on 2024-03-17 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_alter_shedule_class_user_alter_shedule_day_and_more'),
        ('users', '0009_alter_user_class_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='class_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.class', verbose_name='Класс'),
        ),
    ]
