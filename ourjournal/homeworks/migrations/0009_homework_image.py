# Generated by Django 5.0.2 on 2024-03-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0008_rename_author_id_homework_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='homeworks/'),
        ),
    ]
