import ability
from random import choice

class hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        hold = [self.name, opponent.name]
        return f"{choice(hold)} won!"

    def add_ability(self, ability):
        self.abilities.append(ability)
        return

    def add_armor(self, armor):
        self.armors.append(armor)
        return

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, incoming_damage):
        total_damage = incoming_damage
        for armor in self.armors:
            total_damage -= armor.defend()
        return total_damage

    def take_damage(self, damage):
        self.current_health -= damage
        return 

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
        




Ability = ability("Great Debugging", 50)
another_ability = ability("Smarty Pants", 90)
hero = hero("Grace Hopper", 200)
hero.add_ability(ability)
hero.add_ability(another_ability)
print(hero.attack())
