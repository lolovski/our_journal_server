# Generated by Django 5.0.2 on 2024-03-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0010_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'комментарий', 'verbose_name_plural': 'комментарий'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Введите текст комментария', verbose_name='Текст комментария'),
        ),
    ]
