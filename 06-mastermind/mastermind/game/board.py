
import random
from typing import Text

# TODO: Define the Board class here
class Board:

    def __init__(self):
        # contructs the board
        self._hint = None
        self._guessed = False

        self._prepare()

    def apply(self, move):
        # updates hint
        guess = move.get_guess()
        print(guess)
        code = self._code
        hint = move._create_hint(code, guess)
        print("Your guess", "".join(guess), f"your hint {hint}")
        self._hint = hint
    
    def get_hint(self):
        # returns the hint
        return self._hint
        
    def is_guessed(self):
        #ends the game when conditions are met
        hint = self._hint
        if hint == "xxxx":
            return "win"


    def _prepare(self):
        # sets up code
        code = random.randint(1000, 10000)
        self._code = list(str(code))

