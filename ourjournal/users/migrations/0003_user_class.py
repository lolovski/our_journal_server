# Generated by Django 5.0.2 on 2024-03-02 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('users', '0002_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classes.class'),
            preserve_default=False,
        ),
    ]