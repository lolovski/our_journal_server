# Generated by Django 4.0.6 on 2024-03-24 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0017_alter_shedule_class_user_alter_shedule_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.lesson', verbose_name='Урок'),
        ),
        migrations.AlterField(
            model_name='shedule',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
