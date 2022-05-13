from weapon import Weapon

class Robot:

    def __init__(self):
        self.name = 'Bruticus'
        self.health = 100
        self.active_weapon = Weapon('Brutal Blaster', 20)
        
        
    def attack_dinosaur(self, dinosaur):
        self.dinosaur.health -= self.active_weapon 
        

    # Additional names of robots Ratchet and Bluestreak