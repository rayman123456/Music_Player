# Generated by Django 3.2.5 on 2021-08-23 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210823_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]
