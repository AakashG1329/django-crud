# Generated by Django 5.0.4 on 2024-04-12 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.BooleanField()),
                ('isAddToWishList', models.BooleanField()),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'tbl_wishlist',
            },
        ),
    ]
