# Generated by Django 3.1.5 on 2021-01-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210122_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Applicane', 'Applicant'), ('Employer', 'Employer')], max_length=35),
        ),
    ]
