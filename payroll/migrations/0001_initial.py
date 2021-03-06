# Generated by Django 2.2.12 on 2022-03-18 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=20, verbose_name='Employee')),
                ('timein', models.DateTimeField(verbose_name='Time In')),
                ('timeout', models.DateTimeField(verbose_name='Time Out')),
                ('description', models.CharField(choices=[('D', 'Design'), ('L', 'Lunch'), ('O', 'Officework'), ('P', 'Personal'), ('X', 'Other')], max_length=1, verbose_name='Description')),
                ('billable', models.CharField(max_length=10, verbose_name='Billable')),
                ('jobnumber', models.CharField(max_length=10, verbose_name='Job Number')),
            ],
        ),
    ]
