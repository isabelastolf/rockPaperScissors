from enum import Enum
import random


class Shape(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'

class Player:
    def __init__(self):
        self.score = 0
        self.shapes = [Shape.ROCK.name, Shape.PAPER.name, Shape.SCISSOR.name]

    def choose(self):
        while True:
            user_input = input("Please enter your choice: ").upper()
            if(user_input not in self.shapes):
                print("Invalid option")
            return user_input
            
            

class Computer:
    def __init__(self):
        self.score = 0
        self.shapes = [Shape.ROCK.name, Shape.PAPER.name, Shape.SCISSOR.name]

    def choose(self):
        shape_of_choice = random.choice(self.shapes)
        #print(shape_of_choice)
        return shape_of_choice

class Game:
    def __init__(self):
        self.max_round = 3
        self.round = 0
        self.computer = Computer()
        self.player = Player()

    def play(self):
        while (self.round < self.max_round):
            computer_choice = self.computer.choose()
            player_choice = self.player.choose()
            print("Computer plays ",computer_choice)
            self.adjust_score(computer_choice, player_choice)
            print("Round: ", self.round)
            print("Player Score: ", self.player.score)
            print("Computer Score: ", self.computer.score)
        if(self.round == 3):
            if(self.computer.score > self.player.score):
                print("Computer wins")
            elif(self.player.score > self.computer.score):
                print("Player wins")
            else:
                print("Tie")
    
    def adjust_score(self, computer_choice , player_choice):
        #rock > scissor & paper > rock & scissor > paper
        if(computer_choice == player_choice):
            return
        if((computer_choice == Shape.ROCK.name and player_choice == Shape.SCISSOR.name) or \
           (computer_choice == Shape.SCISSOR.name and player_choice == Shape.PAPER.name) or \
           (computer_choice == Shape.PAPER.name and player_choice == Shape.ROCK.name)):
            self.computer.score += 1
        else:
            self.player.score += 1
        self.round += 1

    
if __name__ == "__main__":
    game = Game()
    game.play()
