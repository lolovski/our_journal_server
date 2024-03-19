# Generated by Django 5.0.2 on 2024-03-14 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0010_rename_class_id_shedule_class_user_and_more'),
        ('users', '0008_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='class_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.class'),
        ),
    ]
