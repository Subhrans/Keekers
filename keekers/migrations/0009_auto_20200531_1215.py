# Generated by Django 3.0.1 on 2020-05-31 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keekers', '0008_auto_20200531_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='keekers.OrderItem'),
        ),
    ]