# Generated by Django 2.2.17 on 2021-03-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_image'),
        ),
    ]
