# Generated by Django 3.1.1 on 2020-10-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email address'),
        ),
    ]
