# Generated by Django 5.0.4 on 2024-04-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uicontent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uicontent',
            name='owner',
            field=models.CharField(default='', max_length=255),
        ),
    ]
