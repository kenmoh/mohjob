# Generated by Django 3.1.6 on 2021-02-21 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_job_add_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='add_category',
        ),
    ]
