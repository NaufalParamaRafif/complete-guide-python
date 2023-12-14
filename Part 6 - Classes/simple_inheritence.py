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

class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy)
        super().__init__(health, energy)
        self.speed = speed
        super().move(self.speed)

    def bite(self):
        print("The shark has bitten")

    def move(self):
        print(f"Shark is moved at speed {self.speed}km/h")

shark = Shark(222, 100, 75)
print(shark.energy)