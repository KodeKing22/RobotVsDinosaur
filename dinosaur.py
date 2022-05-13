class Dinosaur:

    def __init__(self):
        self.name = 'Indominus'
        self.attack_power = 25
        self.health = 100
        
    def attack_robot(self, robot):
        robot.health -= self.attack_power
        


# Additional names for other dinosaurs Velociraptor and Megalgon