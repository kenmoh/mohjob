# Generated by Django 3.1.6 on 2021-02-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20210216_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
