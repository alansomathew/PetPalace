# Generated by Django 4.0.4 on 2022-06-04 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_hospitaltype'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place'),
        ),
    ]
