# Generated by Django 5.0.4 on 2024-04-12 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='CategoryId',
            new_name='Category_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='itemNumber',
            new_name='item_number',
        ),
    ]
