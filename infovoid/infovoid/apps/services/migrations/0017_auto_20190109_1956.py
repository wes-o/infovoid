# Generated by Django 2.1.5 on 2019-04-16  

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_remove_medium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
