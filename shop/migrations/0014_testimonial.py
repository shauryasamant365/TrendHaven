# Generated by Django 4.1.4 on 2023-06-01 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_account_auth_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('rating', models.IntegerField(default='')),
                ('review', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
