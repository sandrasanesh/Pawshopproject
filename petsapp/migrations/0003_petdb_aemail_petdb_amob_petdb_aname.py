# Generated by Django 4.2.6 on 2023-12-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsapp', '0002_delete_backendsigndb'),
    ]

    operations = [
        migrations.AddField(
            model_name='petdb',
            name='aemail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='petdb',
            name='amob',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='petdb',
            name='aname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
