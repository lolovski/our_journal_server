# Generated by Django 5.0.2 on 2024-03-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_alter_class_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='school',
            field=models.CharField(max_length=50),
        ),
    ]
