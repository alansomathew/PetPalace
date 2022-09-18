# Generated by Django 4.0.4 on 2022-06-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_newhospital_hospitaltype'),
        ('User', '0004_bookfood'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=50)),
                ('doj', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newuser')),
            ],
        ),
    ]
