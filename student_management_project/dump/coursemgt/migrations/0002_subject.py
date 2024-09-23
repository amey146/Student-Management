# Generated by Django 5.0.7 on 2024-09-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sb_id', models.TextField(primary_key=True, serialize=False)),
                ('sbname', models.CharField(max_length=255)),
                ('courses', models.ManyToManyField(related_name='subjects', to='coursemgt.course')),
            ],
        ),
    ]
