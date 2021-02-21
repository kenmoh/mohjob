# Generated by Django 3.1.6 on 2021-02-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_employerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(choices=[('---------', '---------'), ('Abuja', 'Abuja'), ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Anambra', 'Anambra'), ('Awka', 'Awka'), ('Akwa Ibom', 'Akwa Ibom'), ('Bauch', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross river', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Enugu', 'Enugu'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=35),
        ),
    ]