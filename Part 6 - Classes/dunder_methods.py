class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    def __len__(self):
        return self.health
    def __abs__(self):
        return self.energy
    def __str__(self):
        return f"Monster with health: {self.health}, energy: {self.energy}"
    def __call__(self):
        return f"{self} is called"
    def __add__(self, number):
        return self.health + number
    
    def attack(self, amount = 10):
        print("The monster has attacked!")
        print(f'{amount} of damage was dealt')
        self.energy -= 10
        print(self.energy)

    def move(self, speed=0):
        print(f"Monster is moved at speed {speed}km/h")
    
monster_1 = Monster(100, 90)
# print(len(monster_1))
# print(abs(monster_1))
# print(str(monster_1))
# print(dir(monster_1))
# print(monster_1.__dict__)
# print(vars(monster_1))
# print(monster_1 + 1)
# print(monster_1())
print(str(monster_1))