# Generated by Django 4.0.6 on 2022-07-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_id_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='id_sensor',
            new_name='sensor_id',
        ),
    ]
