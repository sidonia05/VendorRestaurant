# Generated by Django 4.2.1 on 2023-06-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantmenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
    ]
