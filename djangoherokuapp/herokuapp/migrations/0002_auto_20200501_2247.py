# Generated by Django 3.0.5 on 2020-05-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='imagen',
            field=models.URLField(),
        ),
    ]
