from dinosaur import Dinosaur
from robot import Robot

class Battlefield:

    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('Welcome to the battle between Time an d Technology!\nThere can only be one Victor!')

    def battle_phase(self):
        
        while self.robot.health >= 0:
            
            self.dinosaur.attack_robot(self.robot)
            print(f'Indominus attacked Bruticus.\n Bruticus health is now: {self.robot.health}')
            
            self.robot.attack_dinosaur(self.dinosaur)
            print(f'Bruticus attacked Indominus.\n Indominus health is now: {self.dinosaur.health}')
            
            self.display_winner()
                    

    def display_winner(self):
            
            if self.dinosaur.health >= 0:
                print(f' ***{self.dinosaur.name} is the Victor!***')
            
            elif self.robot.health == 0:
                print(f' ***{self.robot.name} is the Victor!***')