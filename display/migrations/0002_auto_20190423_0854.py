# Generated by Django 2.1.5 on 2019-04-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane',
            name='phasefourdate',
            field=models.CharField(default='banana', max_length=100),
        ),
        migrations.AddField(
            model_name='plane',
            name='phaseonedate',
            field=models.CharField(default='banana', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plane',
            name='phasethreedate',
            field=models.CharField(default='banana', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plane',
            name='phasetwodate',
            field=models.CharField(default='banana', max_length=100),
            preserve_default=False,
        ),
    ]
