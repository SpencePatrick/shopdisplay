# Generated by Django 2.1.5 on 2019-04-23 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_auto_20190423_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='phasefourdate',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='phaseonedate',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='phasethreedate',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='phasetwodate',
        ),
    ]
