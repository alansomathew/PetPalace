# Generated by Django 4.0.4 on 2022-06-09 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_newfooditem'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpet',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.newpets'),
        ),
    ]
