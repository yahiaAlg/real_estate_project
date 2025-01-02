# Generated by Django 5.1.4 on 2025-01-01 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_photo_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.listing')),
            ],
        ),
    ]
