# Generated by Django 4.0.4 on 2022-06-15 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackdoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=50)),
                ('doj', models.DateField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.newdoctor')),
            ],
        ),
    ]
