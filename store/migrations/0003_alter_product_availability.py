# Generated by Django 4.1.7 on 2024-01-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_options_product_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
