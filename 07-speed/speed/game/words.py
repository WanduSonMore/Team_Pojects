#
# Suggestions:
#   - It is convention that class names are capitalized, such as Words or Buffer
#   - _position and _velocity are private attributes of the Actor class, you shouldn't use them. You can use the set_position and set_velocity methods instead
#

import random 
from game.actor import Actor
from game.point import Point
class words(Actor):
    def __init__(self):
        super().__init__()
        self._position = ()
        self._velocity = Point(random.randint(-1, 1), random.randint(-1, 1))
        
    def reset_word():
        pass

    def word_check(self, letters_typed):
        if letters_typed == #word:
            #reset specific word
            
            return True
