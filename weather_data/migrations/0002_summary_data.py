# Generated by Django 3.2.7 on 2021-09-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_temperature', models.FloatField()),
                ('averge_humidity', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]