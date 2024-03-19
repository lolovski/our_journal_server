# Generated by Django 5.0.2 on 2024-03-02 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.status'),
            preserve_default=False,
        ),
    ]
