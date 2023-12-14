class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount = 10):
        print(f"The monster has attacked!")
        print(f'{amount} of damage was dealt')
        self.energy -= 10

    def move(self, speed=0):
        print(f"Monster is moved at speed {speed}km/h")

class Scorpion(Monster):
    def __init__(self, poison_damage, energy, health):
        super().__init__(health, energy)
        self.poison_damage = poison_damage
    def attack(self):
        print(f"The scorpion has attacked!")
        print(f'{self.poison_damage} of poison damage was dealt')

first_scorpion = Scorpion(342, 87, 100)
first_scorpion.attack()
print(first_scorpion.energy)