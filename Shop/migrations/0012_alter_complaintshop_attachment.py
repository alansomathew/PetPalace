# Generated by Django 4.0.4 on 2022-06-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_newfooditem_fooditemdetails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintshop',
            name='attachment',
            field=models.FileField(null=True, upload_to='Uploads/attachmentshop/'),
        ),
    ]
