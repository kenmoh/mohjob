# Generated by Django 3.1.6 on 2021-02-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210216_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=21, null=True, unique=True),
        ),
    ]
