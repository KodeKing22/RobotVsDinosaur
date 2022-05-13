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
        print('Welcome to the battle between Time and Technology!\nThere can only be one Victor!')

    def battle_phase(self):
        
        while self.dinosaur.attack_robot(self.robot):
                print(f'Indominus attacked Bruticus.\n Bruticus health is now: {self.robot.health}')
            
                if self.robot.attack_dinosaur(self.dinosaur):
                    print(f'Bruticus attacked Indominus.\n Indominus health is now: {self.dinosaur.health}')
            
                elif self.robot.health <= 0 or self.dinosaur.health <= 0:
                    display_winner = self.robot.health or self.dinosaur.health <= 0 
                    print(display_winner)
                    

    def display_winner(self):
            
            if self.dinosaur.health >= 1:
                print(f'Opponent defeated!\n   ***{self.dinosaur.name} is the Victor!***')
            
            elif self.robot.health >= 1:
                print(f'Opponent defeated!\n   ***{self.robot.name} is the Victor!***')