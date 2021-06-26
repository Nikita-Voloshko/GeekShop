# Generated by Django 2.2.17 on 2021-04-14 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='product_image')),
                ('description', models.TextField(blank=True)),
                ('Short_description', models.TextField(blank=True, max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mineapp.ProductCategory')),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]
