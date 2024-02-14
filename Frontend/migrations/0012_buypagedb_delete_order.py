# Generated by Django 4.2.6 on 2023-12-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0011_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='buypagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('final_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]