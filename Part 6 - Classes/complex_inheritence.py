class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
    
    def attack(self, amount_damage=0):
        print(f"Monster attack something with the damage of {amount_damage}")
    def move(self, speed=0):
        print(f"Monster move at speed of {speed}km/h")

class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)
    def swim(self):
        print(f"fish swimming at the speed of {self.speed}km/h")

class Shark(Monster, Fish):
    def __init__(self, bite_strength:int, health:int, energy:int, speed:int, has_scales:bool):
        self.bite_strength = bite_strength
        super().__init__(health, energy, speed=speed, has_scales=has_scales)
    def bite(self):
        print(f"shark bite something with the damage of {self.bite_strength}")

first_shark = Shark(bite_strength=25, health=100, energy=75, speed=200, has_scales=False)
