from weapon import Weapon

class Robot:

    def __init__(self):
        self.name = 'Bruticus'
        self.health = 100
        self.active_weapon = Weapon('Brutal Blaster', 20)
        
        
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power 
        

    # Additional names of robots Ratchet and Bluestreak