# Generated by Django 2.2.4 on 2019-09-01 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medico',
            options={'permissions': {('is_medico', 'Usuario Medico')}},
        ),
    ]
