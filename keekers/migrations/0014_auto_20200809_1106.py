# Generated by Django 3.0.1 on 2020-08-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keekers', '0013_auto_20200809_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='p_image_sub_1',
            field=models.ImageField(blank=True, null=True, upload_to='images//'),
        ),
        migrations.AlterField(
            model_name='item',
            name='p_image_sub_2',
            field=models.ImageField(blank=True, null=True, upload_to='images//'),
        ),
        migrations.AlterField(
            model_name='item',
            name='p_image_sub_3',
            field=models.ImageField(blank=True, null=True, upload_to='images//'),
        ),
    ]