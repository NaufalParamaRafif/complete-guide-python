class Hero:
    def __init__(self, damage):
        self.damage = damage
    def attack(self, monster):
        monster.get_damage(self.damage)

class Monster:
    def __init__(self, health):
        self.health = health
    def get_damage(self, amount_damage):
        self.health -= amount_damage

first_monster = Monster(health=100)
first_hero = Hero(damage=15)
first_hero.attack(monster=first_monster)
print(first_monster.health)