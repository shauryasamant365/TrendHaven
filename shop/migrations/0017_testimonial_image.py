# Generated by Django 4.1.4 on 2023-06-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_testimonial_designation_alter_testimonial_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='', upload_to='media/testimonials/images/'),
        ),
    ]
