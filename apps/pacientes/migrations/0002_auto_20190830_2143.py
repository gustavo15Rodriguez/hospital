# Generated by Django 2.2.4 on 2019-08-31 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjetavisita',
            name='hora_comienzo',
            field=models.DateTimeField(),
        ),
    ]
