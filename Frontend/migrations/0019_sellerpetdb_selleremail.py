# Generated by Django 4.2.6 on 2023-12-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0018_remove_cartdb_fimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerpetdb',
            name='selleremail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
