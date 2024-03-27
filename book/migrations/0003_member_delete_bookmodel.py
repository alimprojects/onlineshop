# Generated by Django 5.0.3 on 2024-03-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_membersmodel_bookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('joined_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='bookModel',
        ),
    ]
