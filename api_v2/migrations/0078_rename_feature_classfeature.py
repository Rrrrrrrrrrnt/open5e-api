# Generated by Django 3.2.20 on 2024-05-25 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0077_rename_featureitem_classfeatureitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feature',
            new_name='ClassFeature',
        ),
    ]