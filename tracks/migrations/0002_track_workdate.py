# Generated by Django 4.2 on 2023-08-10 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='workDate',
            field=models.DateField(null=True, verbose_name='Work Date'),
        ),
    ]
