# Generated by Django 3.0.5 on 2020-05-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0005_auto_20200502_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='herokuapp.Ingrediente'),
        ),
    ]
