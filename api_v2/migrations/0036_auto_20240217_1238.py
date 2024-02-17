# Generated by Django 3.2.20 on 2024-02-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0035_auto_20240216_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='higher_level',
            field=models.TextField(default='', help_text="Description of casting the spell at a different level.'"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='school',
            field=models.TextField(choices=[('abjuration', 'Abjuration'), ('conjuration', 'Conjuration'), ('divination', 'Divination'), ('enchantment', 'Enchantment'), ('evocation', 'Evocation'), ('illusion', 'Illusion'), ('necromancy', 'Necromancy'), ('transmutation', 'Transmutaion')], default='', help_text="Spell school, such as 'Evocation'"),
            preserve_default=False,
        ),
    ]
