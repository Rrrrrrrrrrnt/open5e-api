# Generated by Django 3.2.20 on 2024-06-27 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0100_auto_20240619_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='burrow',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='climb',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='fly',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_acrobatics',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to acrobatics skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_animal_handling',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to animal handling skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_arcana',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to arcana skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_athletics',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to athletics skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_deception',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to deception skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_history',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to history skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_insight',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to insight skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_intimidation',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to intimidation skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_investigation',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to investigation skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_medicine',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to medicine skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_nature',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to nature skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_perception',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to perception skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_performance',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to performance skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_persuasion',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to persuasion skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_religion',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to religion skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_sleight_of_hand',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to sleight of hand skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_stealth',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to stealth skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='skill_bonus_survival',
            field=models.SmallIntegerField(blank=True, help_text='Signed integer added to survival skill checks.', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='swim',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='creature',
            name='unit',
            field=models.CharField(blank=True, choices=[('feet', 'feet'), ('miles', 'miles')], help_text='What distance unit the relevant field uses.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='creature',
            name='walk',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='document',
            name='distance_unit',
            field=models.CharField(blank=True, choices=[('feet', 'feet'), ('miles', 'miles')], help_text='What distance unit the relevant field uses.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='damage_types',
            field=models.JSONField(blank=True, default=list, help_text='The types of damage done by the spell in a list.'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='duration',
            field=models.TextField(choices=[('instantaneous', 'instantaneous'), ('instantaneous or special', 'instantaneous or special'), ('1 turn', '1 turn'), ('1 round', '1 round'), ('concentration + 1 round', 'concentration + 1 round'), ('2 rounds', '2 rounds'), ('3 rounds', '3 rounds'), ('4 rounds', '4 rounds'), ('1d4+2 rounds', '1d4+2 rounds'), ('5 rounds', '5 rounds'), ('6 rounds', '6 rounds'), ('10 rounds', '10 rounds'), ('up to 1 minute', 'up to 1 minute'), ('1 minute', '1 minute'), ('1 minute, or until expended', '1 minute, or until expended'), ('1 minute, until expended', '1 minute, until expended'), ('1 minute', '1 minute'), ('5 minutes', '5 minutes'), ('10 minutes', '10 minutes'), ('1 minute or 1 hour', '1 minute or 1 hour'), ('up to 1 hour', 'up to 1 hour'), ('1 hour', '1 hour'), ('1 hour or until triggered', '1 hour or until triggered'), ('2 hours', '2 hours'), ('3 hours', '3 hours'), ('1d10 hours', '1d10 hours'), ('6 hours', '6 hours'), ('2-12 hours', '2-12 hours'), ('up to 8 hours', 'up to 8 hours'), ('8 hours', '8 hours'), ('1 hour/caster level', '1 hour/caster level'), ('10 hours', '10 hours'), ('12 hours', '12 hours'), ('24 hours or until the target attempts a third death saving throw', '24 hours or until the target attempts a third death saving throw'), ('24 hours', '24 hours'), ('1 day', '1 day'), ('3 days', '3 days'), ('5 days', '5 days'), ('7 days', '7 days'), ('10 days', '10 days'), ('13 days', '13 days'), ('30 days', '30 days'), ('1 year', '1 year'), ('special', 'special'), ('until dispelled or destroyed', 'until dispelled or destroyed'), ('until destroyed', 'until destroyed'), ('until dispelled', 'until dispelled'), ('until cured or dispelled', 'until cured or dispelled'), ('until dispelled or triggered', 'until dispelled or triggered'), ('permanent until discharged', 'permanent until discharged'), ('permanent; one generation', 'permanent; one generation'), ('permanent', 'permanent')], help_text='Description of the duration of the effect such as "instantaneous" or "1 minute"'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='higher_level',
            field=models.TextField(blank=True, help_text='Description of casting the spell at a different level.'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='range',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='spell',
            name='range_unit',
            field=models.CharField(blank=True, choices=[('feet', 'feet'), ('miles', 'miles')], help_text='What distance unit the relevant field uses.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='shape_size',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='spell',
            name='shape_size_unit',
            field=models.CharField(blank=True, choices=[('feet', 'feet'), ('miles', 'miles')], help_text='What distance unit the relevant field uses.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='shape_type',
            field=models.TextField(blank=True, choices=[('cone', 'Cone'), ('cube', 'Cube'), ('cylinder', 'Cylinder'), ('line', 'Line'), ('sphere', 'sphere')], help_text='The shape of the area of effect.', null=True),
        ),
    ]
