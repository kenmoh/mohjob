# Generated by Django 3.1.5 on 2021-01-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('Applicane', 'Applicant'), ('Employer', 'Employer')], max_length=35, null=True),
        ),
    ]
