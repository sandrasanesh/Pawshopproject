# Generated by Django 4.2.6 on 2023-12-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0013_remove_buypagedb_final_price_remove_buypagedb_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]