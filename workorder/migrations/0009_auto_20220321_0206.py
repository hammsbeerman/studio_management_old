# Generated by Django 2.2.12 on 2022-03-21 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorder', '0008_auto_20220321_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='material',
            field=models.ManyToManyField(blank=True, to='inventory.Inventory'),
        ),
    ]
