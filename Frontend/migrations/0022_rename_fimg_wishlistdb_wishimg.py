# Generated by Django 4.2.6 on 2023-12-25 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0021_remove_notificationdb_petimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistdb',
            old_name='fimg',
            new_name='wishimg',
        ),
    ]