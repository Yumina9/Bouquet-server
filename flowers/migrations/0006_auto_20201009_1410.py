# Generated by Django 3.1.1 on 2020-10-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0005_auto_20201009_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
