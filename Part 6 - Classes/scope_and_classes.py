# def update_health(amount):
#     health += amount
# health = 10
# print(health)
# update_health(20)
# print(health)

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_health(self, amount_health):
        self.health = amount_health

    def update_energy(self, amount_energy):
        self.energy = amount_energy
            
monster = Monster(health= 100, energy=75)
print(monster.health)