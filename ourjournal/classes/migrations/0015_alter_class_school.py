# Generated by Django 4.0.6 on 2024-03-22 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0014_rename_count_student_class_count_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='classes.school'),
        ),
    ]
