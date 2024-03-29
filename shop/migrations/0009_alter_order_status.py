# Generated by Django 4.1.4 on 2023-05-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('suspended', 'Suspended')], default='pending', max_length=20),
        ),
    ]
