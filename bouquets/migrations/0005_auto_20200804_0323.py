# Generated by Django 3.0.8 on 2020-08-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouquets', '0004_auto_20200804_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='flower_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
