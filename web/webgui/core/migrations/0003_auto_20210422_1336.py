# Generated by Django 3.1.7 on 2021-04-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210422_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='name',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
