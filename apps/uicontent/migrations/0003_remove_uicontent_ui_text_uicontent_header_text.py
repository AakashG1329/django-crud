# Generated by Django 5.0.4 on 2024-04-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uicontent', '0002_uicontent_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uicontent',
            name='ui_text',
        ),
        migrations.AddField(
            model_name='uicontent',
            name='header_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]