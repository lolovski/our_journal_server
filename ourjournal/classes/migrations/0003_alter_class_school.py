# Generated by Django 5.0.2 on 2024-03-08 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.school'),
        ),
    ]
