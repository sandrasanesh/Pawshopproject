# Generated by Django 4.2.6 on 2023-11-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_adrsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlistdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]