# Generated by Django 3.2.5 on 2021-08-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210823_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
