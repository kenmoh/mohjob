# Generated by Django 3.1.6 on 2021-02-16 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='profile',
        ),
    ]