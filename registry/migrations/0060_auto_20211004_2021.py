# Generated by Django 3.2.7 on 2021-10-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0059_auto_20211004_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='make',
            field=models.CharField(blank=True, help_text='Enter aircraft make ', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='master_series',
            field=models.CharField(blank=True, help_text='Specify the master series', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='popular_name',
            field=models.CharField(blank=True, help_text='Enter popular name for this aircraft', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='series',
            field=models.CharField(blank=True, help_text='Enter aircraft production series', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='historicalaircraft',
            name='make',
            field=models.CharField(blank=True, help_text='Enter aircraft make ', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='historicalaircraft',
            name='master_series',
            field=models.CharField(blank=True, help_text='Specify the master series', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='historicalaircraft',
            name='popular_name',
            field=models.CharField(blank=True, help_text='Enter popular name for this aircraft', max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='historicalaircraft',
            name='series',
            field=models.CharField(blank=True, help_text='Enter aircraft production series', max_length=280, null=True),
        ),
    ]