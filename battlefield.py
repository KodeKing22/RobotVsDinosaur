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
        self.dinosaur.attack_robot(self.robot)
        print(f'{self.dinosaur} attacked {self.robot}\n {self.robot} health is now: {self.robot.health}')
        pass

    # def display_winner(self):
    #     print('Opponent defeated!)