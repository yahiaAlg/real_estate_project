# Generated by Django 5.1.4 on 2024-12-31 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_photo_2_alter_listing_photo_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='listings/%Y/%M/%d'),
        ),
    ]
