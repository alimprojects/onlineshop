# Generated by Django 5.0.3 on 2024-03-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_contacts_products_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
