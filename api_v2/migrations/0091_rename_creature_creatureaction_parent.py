# Generated by Django 3.2.20 on 2024-06-01 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0090_auto_20240601_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creatureaction',
            old_name='creature',
            new_name='parent',
        ),
    ]
