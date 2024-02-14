# Generated by Django 4.2.6 on 2023-11-26 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_wishlistdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_des', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Frontend.cartdb')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Frontend.signupdb')),
            ],
        ),
    ]