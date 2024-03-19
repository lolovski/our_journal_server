# Generated by Django 5.0.2 on 2024-03-17 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_alter_shedule_class_user_alter_shedule_day_and_more'),
        ('homeworks', '0011_alter_comment_options_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='class_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='classes.class', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='classes.shedule', verbose_name='Урок'),
        ),
    ]