# Generated by Django 5.0.4 on 2024-04-12 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='orderStatus',
            new_name='order_status',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='productId',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='userId',
            new_name='user_id',
        ),
    ]
