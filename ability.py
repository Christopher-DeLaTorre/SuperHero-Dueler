import hero
import random

class ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        attack = random.randint(0, self.max_damage)
        return attack

ability = ability("Debugging Shot", 10)
print(ability.name)
print(ability.attack())

