# Generated by Django 3.2.5 on 2021-08-23 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='song',
            name='image',
        ),
    ]
