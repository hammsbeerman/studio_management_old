# Generated by Django 2.2.12 on 2022-03-18 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20220318_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
    ]