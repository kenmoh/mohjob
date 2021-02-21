# Generated by Django 3.1.6 on 2021-02-16 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20210216_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.jobcategory'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(default='Testing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
