# Generated by Django 3.0.8 on 2021-08-22 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
    ]
