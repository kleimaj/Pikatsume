# Generated by Django 3.0.4 on 2020-03-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200322_2116'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ptype',
        ),
        migrations.AlterField(
            model_name='profile',
            name='pikachu',
            field=models.ManyToManyField(to='main_app.Pika'),
        ),
    ]
