# Generated by Django 4.0.4 on 2022-06-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_adminlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='newshop',
            name='shopownercontact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='newshop',
            name='shopownername',
            field=models.CharField(max_length=50, null=True),
        ),
    ]