# Generated by Django 4.2.6 on 2023-11-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0007_remove_reviewdb_item_remove_reviewdb_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistdb',
            name='quantity',
        ),
        migrations.AddField(
            model_name='wishlistdb',
            name='des',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='wishlistdb',
            name='fimg',
            field=models.ImageField(blank=True, null=True, upload_to='wishlist_img'),
        ),
    ]
