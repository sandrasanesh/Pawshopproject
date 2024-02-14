# Generated by Django 4.2.6 on 2023-12-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='backendsigndb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('re_pass', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='catedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('pdes', models.CharField(blank=True, max_length=50, null=True)),
                ('pimg', models.ImageField(blank=True, null=True, upload_to='profile_img')),
            ],
        ),
        migrations.CreateModel(
            name='fooddb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('sname', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('des', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('fimg', models.ImageField(blank=True, null=True, upload_to='food_img')),
            ],
        ),
        migrations.CreateModel(
            name='petdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('breed', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('petimg', models.ImageField(blank=True, null=True, upload_to='pet_img')),
            ],
        ),
        migrations.CreateModel(
            name='shopdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(blank=True, max_length=50, null=True)),
                ('simg', models.ImageField(blank=True, null=True, upload_to='shop_img')),
            ],
        ),
    ]
