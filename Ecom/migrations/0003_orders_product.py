# Generated by Django 3.0.8 on 2021-08-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0002_remove_orders_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.CharField(default='', max_length=900),
        ),
    ]
