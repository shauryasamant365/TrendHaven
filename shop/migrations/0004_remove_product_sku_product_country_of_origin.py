# Generated by Django 4.1.4 on 2023-05-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='product',
            name='country_of_origin',
            field=models.CharField(default='India', max_length=15),
        ),
    ]