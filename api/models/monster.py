
import json

from django.db import models

from .models import GameContent
from .spell import Spell


class Monster(GameContent):
    size = models.TextField(help_text='Monster size category.')

    SIZE_MAPPING = {
    'tiny': 0,
    'small': 1,
    'medium': 2,
    'large': 3,
    'huge': 4,
    'gargantuan': 5,
    'titanic': 6,
    }

    @property
    def size_id(self):
        # Convert the size to lowercase for case-insensitive comparison
        lowercase_size = self.size.lower()

        # Return the size_rating based on the mapping or default to 0 if not found
        return self.SIZE_MAPPING.get(lowercase_size, 0)



    type = models.TextField(
        help_text='The type of the monster, such as "aberration"')
    subtype = models.TextField(
        help_text='If applicable, the subtype of the monster, such as "shapechanger"')
    group = models.TextField(
        null=True,
        help_text='Used to group similar creatures at different stages. "Green Dragon"')
    alignment = models.TextField(
        help_text='Short description of the creature alignment, such as "lawful good"')
    armor_class = models.IntegerField(
        default=12, help_text='Integer representing the armor class.')
    armor_desc = models.TextField(
        null=True, help_text='Description of the armor or armor type.')
    hit_points = models.IntegerField(
        null=True, help_text='Integer of the hit points.')
    hit_dice = models.TextField(
        help_text='Dice string representing a way to calculate hit points.')
    speed_json = models.TextField()

    def speed(self):
        return json.loads(self.speed_json)

    environments_json = models.TextField(
        null=True,
        help_text='String list of environments that the monster can be found in.')

    def environments(self):
        return json.loads(self.environments_json or "[]")

    strength = models.IntegerField(
        null=True, help_text='Integer representing the strength score.')
    dexterity = models.IntegerField(
        null=True, help_text='Integer represeting the dexterity score.')
    constitution = models.IntegerField(
        null=True, help_text='Integer representing the constitution score.')
    intelligence = models.IntegerField(
        null=True, help_text='Integer representing the intelligence score.')
    wisdom = models.IntegerField(
        null=True, help_text='Integer representing the wisdom score.')
    charisma = models.IntegerField(
        null=True, help_text='Integer representing the charisma score.')
    strength_save = models.IntegerField(
        null=True, help_text='Integer representing the strength save.')
    dexterity_save = models.IntegerField(
        null=True, help_text='Integer representing the dexterity save.')
    constitution_save = models.IntegerField(
        null=True, help_text='Integer representing the constitution save.')
    intelligence_save = models.IntegerField(
        null=True, help_text='Integer representing the intelligence save')
    wisdom_save = models.IntegerField(
        null=True, help_text='Integer representing the wisdom save.')
    charisma_save = models.IntegerField(
        null=True, help_text='Integer representing the charisma save.')
    perception = models.IntegerField(
        null=True, help_text='Integer representing the passive perception score.')
    skills_json = models.TextField()

    def skills(self):
        return json.loads(self.skills_json or "{}")
    damage_vulnerabilities = models.TextField(
        help_text='Comma separated list of damage types the monster is vulnerable to.')
    damage_resistances = models.TextField(
        help_text='Comma separated list of damage types the monster is resistant to.')
    damage_immunities = models.TextField(
        help_text='Comma separated list of damage types the monster is immune to.')
    condition_immunities = models.TextField(
        help_text='Comma separated list of conditions the monster is immune to.')
    senses = models.TextField(
        'Comma separated list of senses, such as "blindsight 60ft."')
    languages = models.TextField(
        'Comma separated list of languages that the monster speaks.')
    challenge_rating = models.TextField(help_text='Monster challenge rating.')
    cr = models.FloatField(
        null=True,
        help_text='Monster challenge rating as a float.')
    
    # a list of actions in json text.
    actions_json = models.TextField()  

    def actions(self):
        return json.loads(self.actions_json or "[]")
      
    bonus_actions_json = models.TextField(default=None, null=True)
    
    def bonus_actions(self):
        return json.loads(self.bonus_actions_json or "[]")
    
    # A list of special abilities in json text.
    special_abilities_json = models.TextField()

    def special_abilities(self):
        return json.loads(self.special_abilities_json)
    
    # A list of reactions in json text.
    reactions_json = models.TextField()  

    def reactions(self):
        return json.loads(self.reactions_json)
    
    # a list of legendary actions in json.
    legendary_desc = models.TextField()
    legendary_actions_json = models.TextField()

    def legendary_actions(self):
        return json.loads(self.legendary_actions_json)

    # a list of mythic actions in json.
    mythic_actions_json = models.TextField(null=True, blank=True)

    def mythic_actions(self):
       try:
           return json.loads(self.mythic_actions_json)
       except TypeError as e:
           return None

    # a list of Lair actions in json.
    lair_desc = models.TextField(null=True, blank=True)
    lair_actions_json = models.TextField(null=True, blank=True)

    def lair_actions(self):
        try:
            return json.loads(self.lair_actions_json)
        except TypeError as e:
            return None

    spells_json = models.TextField()
    spell_list = models.ManyToManyField(
        Spell,
        related_name='monsters',
        symmetrical=True,
        through="monsterSpell")
    route = models.TextField(default="monsters/")
    img_main = models.URLField(null=True)

    @staticmethod
    def plural_str() -> str:
        """Return a string specifying the plural name of this model."""
        return "Monsters"

    def search_result_extra_fields(self):
        return {
            "armor_class":self.armor_class,
            "hit_points":self.hit_points,
            "hit_dice":self.hit_dice,
            "strength":self.strength,
            "dexterity":self.dexterity,
            "constitution":self.constitution,
            "intelligence":self.intelligence,
            "wisdom":self.wisdom,
            "charisma":self.charisma,
            "challenge_rating":self.challenge_rating,
            "cr":self.cr
              }

class MonsterSpell(models.Model):
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    @staticmethod
    def plural_str() -> str:
        """Return a string specifying the plural name of this model."""
        return "MonsterSpells"