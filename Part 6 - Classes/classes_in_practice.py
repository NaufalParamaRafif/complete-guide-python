class Monster:
    health = 100
    energy = 50

    def attack(self, amount = 10):
        print("The monster has attacked!")
        # print(self) # same as first_monster object
        print(f'{amount} of damage was dealt')
        self.energy -= 10
        print(self.energy)

    def move(self, speed=0):
        print(f"Monster is moved at speed {speed}km/h")
first_monster = Monster()
# print(first_monster)
# print(first_monster.energy)
# first_monster.attack(100)
# print(first_monster.energy)
first_monster.move(30)