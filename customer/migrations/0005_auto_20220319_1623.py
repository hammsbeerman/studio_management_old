# Generated by Django 2.2.12 on 2022-03-19 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20220318_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='company',
            new_name='customer',
        ),
    ]
