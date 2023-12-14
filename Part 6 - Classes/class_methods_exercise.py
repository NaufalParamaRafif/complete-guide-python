print("====EXERCISE====")

class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite(self):
        print("The monster is bitting")
    def strike(self):
        print("The monster is striking")
    def slash(self):
        print("The monster is slashing")
    def kick(self):
        print("The monster is kicking")

first_monster = Monster(func=Attacks().bite)
first_monster.func()