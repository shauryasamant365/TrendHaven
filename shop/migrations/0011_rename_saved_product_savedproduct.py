# Generated by Django 4.1.4 on 2023-05-29 15:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0010_saved_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='saved_product',
            new_name='SavedProduct',
        ),
    ]
