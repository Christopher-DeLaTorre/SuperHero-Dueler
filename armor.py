import hero
import random

class armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block

armor = armor("Debugging Shield", 10)
print(armor.name)
print(armor.block())