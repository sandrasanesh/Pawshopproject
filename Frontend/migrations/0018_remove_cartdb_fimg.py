# Generated by Django 4.2.6 on 2023-12-11 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0017_cartdb_fimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='fimg',
        ),
    ]