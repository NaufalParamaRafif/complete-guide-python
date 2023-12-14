class Monster:
    '''
        Object that has health, energy attributes, and attack, move methods
    '''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        # private attributes
        self._id = 145

    def attack(self, damage):
        print(f"Monster attack something with the {damage} of damage")
        self.energy -= 10

    def move(self, speed):
        print(f"Monster has moved, at speed of {speed}km/h")

first_monster = Monster(100, 100)
# if hasattr(first_monster, 'health'):
#     print("monster has health attribute")



# def regen():
#     print("Monster has regen")

# monster_attribute_and_value = (['weapon', 'axe'], ['first_skill', regen])

# for attribute, value in monster_attribute_and_value:
#     setattr(first_monster,attribute,value)

# print(first_monster.weapon)

# first_monster.first_skill()



# help(first_monster)
print(first_monster.__doc__)