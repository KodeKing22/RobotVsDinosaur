from weapon import Weapon

class Robot:

    def __init__(self):
        self.name = 'Bruticus'
        self.health = 100
        self.active_weapon = Weapon('Brutal Blaster', 20)
        
        
    def attack_dino(self, dinosaur):
        dinosaur.health -= self.active_weapon
        pass