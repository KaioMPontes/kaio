# Generated by Django 4.0.2 on 2022-10-03 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichas',
            name='user',
        ),
    ]
