# Generated by Django 2.2.4 on 2019-09-01 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='cama',
            field=models.IntegerField(),
        ),
    ]
