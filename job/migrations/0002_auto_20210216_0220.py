# Generated by Django 3.1.6 on 2021-02-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
