# Generated by Django 5.0.1 on 2024-02-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowershop', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]