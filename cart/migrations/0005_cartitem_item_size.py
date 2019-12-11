# Generated by Django 3.0 on 2019-12-11 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_apply_sizes'),
        ('cart', '0004_auto_20191207_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='item_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.SizeChart'),
        ),
    ]
