# Generated by Django 5.0.7 on 2024-09-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmgt', '0007_alter_student_batch_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='st_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]