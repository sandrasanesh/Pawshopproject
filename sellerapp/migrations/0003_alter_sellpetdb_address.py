# Generated by Django 4.2.6 on 2023-10-31 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0002_sellpetdb_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellpetdb',
            name='address',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
