# Generated by Django 3.1.1 on 2020-09-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0003_flower_shops'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
