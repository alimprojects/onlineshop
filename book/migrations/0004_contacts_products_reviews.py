# Generated by Django 5.0.3 on 2024-03-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_member_delete_bookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('supplier_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('unit', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('photo', models.ImageField(upload_to='images/products')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=200)),
                ('review', models.TextField()),
                ('rate', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
