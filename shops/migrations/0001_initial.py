# Generated by Django 3.1.1 on 2020-10-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('florist', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
