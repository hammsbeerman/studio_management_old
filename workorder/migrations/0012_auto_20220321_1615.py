# Generated by Django 2.2.12 on 2022-03-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorder', '0011_auto_20220321_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deadline'),
        ),
    ]
