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
        return

    def attack(self):
        return

    def defend(self, incoming_damage):
        return

    def take_damage(self, damage):
        return

    def is_alive(self):
        return




evil = hero("Joker", 150)
my_hero = hero("Grace Hopper", 200)
print(my_hero.name)
print(my_hero.current_health)
print(my_hero.fight(evil))
