# Generated by Django 4.2 on 2023-08-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_track_workdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='compleateDate',
            field=models.DateField(blank=True, null=True, verbose_name='Compleate Date'),
        ),
        migrations.AlterField(
            model_name='track',
            name='workDate',
            field=models.DateField(blank=True, null=True, verbose_name='Work Date'),
        ),
    ]
