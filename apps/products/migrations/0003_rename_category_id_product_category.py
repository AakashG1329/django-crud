# Generated by Django 5.0.4 on 2024-04-12 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_categoryid_product_category_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category_id',
            new_name='Category',
        ),
    ]
