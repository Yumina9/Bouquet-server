# Generated by Django 3.1.1 on 2020-10-16 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ribbons', '0001_initial'),
        ('shops', '0001_initial'),
        ('wrappingPapers', '0001_initial'),
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='image')),
                ('bouquet_paper_price', models.IntegerField(blank=True, null=True)),
                ('flower_count', models.IntegerField(blank=True, null=True)),
                ('flower', models.ManyToManyField(blank=True, null=True, to='flowers.Flower')),
                ('ribbon', models.ManyToManyField(blank=True, null=True, to='ribbons.Ribbon')),
                ('shops', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
                ('wrappingpaper', models.ManyToManyField(blank=True, null=True, to='wrappingPapers.WrappingPaper')),
            ],
        ),
    ]
