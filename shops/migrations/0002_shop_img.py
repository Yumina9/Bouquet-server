# Generated by Django 3.1.1 on 2020-10-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
