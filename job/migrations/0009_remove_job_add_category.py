# Generated by Django 3.1.6 on 2021-02-20 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_remove_job_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='add_category',
        ),
    ]
