# Generated by Django 4.1.4 on 2023-06-01 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_testimonial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='mobile_number',
        ),
    ]
