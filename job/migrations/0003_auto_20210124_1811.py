# Generated by Django 3.1.5 on 2021-01-24 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20210122_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='posted_by',
            new_name='user',
        ),
    ]
