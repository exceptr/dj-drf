# Generated by Django 4.0.6 on 2022-07-22 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_alter_measurement_sensor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
