# Generated by Django 4.2.6 on 2023-11-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0009_sellerpetdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistdb',
            name='fimg',
            field=models.ImageField(blank=True, null=True, upload_to='food_img'),
        ),
    ]