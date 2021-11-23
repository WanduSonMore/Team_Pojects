#director
#guesser or user
#console
#updator
import random
from game.updater import updater
from game.console import console
from game.guesser import guesser
from game.word_bank import word_bank
class Director:
    #runs the game
    
    def __init__(self):
        self.chosen_word = random.choice(word_bank)
        self.split_word = list(self.chosen_word)
        self.guessor = guesser()
        self.console = console()
        self.updator = updater()
        self.guesses = 0
        self.guess = ['']
        self.checked_guess = ['']
        self.lines = []
        self.fail = 0
        self.keep_playing = True
    def game_start(self):
        #starts the game
        for i in self.split_word:
            self.lines.append('_')
            
        while self.keep_playing:
            self.get_input()
            self.do_update()
            self.display_game()
        
        
    def get_input(self):
        if self.guesses == 0:
            self.console.show_lines(self.lines)
            self.guess.append(self.guessor.user_first())
            self.guesses += 1

        else:
            self.guess[-1] = self.guessor.user(self.checked_guess[-1])
        


    def do_update(self):
        self.checked_guess[-1], self.lines, self.fail = self.updator.guess_check(self.guess[-1], self.split_word, self.lines)
        self.keep_playing = self.updator.can_play(self.lines)

    def display_game(self):
        self.console.show_lines(self.lines)
        self.console.show_letters(self.guess[-1])
        self.console.jumper_show(self.fail, self.chosen_word)
        