# Generated by Django 4.0.6 on 2022-07-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_rename_id_sensor_measurement_sensor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sensor', to='measurement.sensor'),
        ),
    ]
