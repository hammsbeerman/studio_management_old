# Generated by Django 2.2.12 on 2022-03-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorder', '0002_auto_20220319_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deadline'),
        ),
    ]