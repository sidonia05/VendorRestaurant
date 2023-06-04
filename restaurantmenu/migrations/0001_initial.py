# Generated by Django 4.2.1 on 2023-06-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/media/images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('type_prod', models.CharField(choices=[('1', 'Bakery'), ('2', 'Mexican food'), ('3', 'Fastfood'), ('4', 'Pizza'), ('5', 'Salad'), ('6', 'Traditional food')], max_length=30, null=True)),
                ('um', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
