#
# Suggestions:
#   - It is convention that class names are capitalized, such as Words or Buffer
#   - _text is a property of the Actor that is private, therefore you shouldn't be using it in the subclass
#

from game.actor import Actor
from game import constants
from game.point import Point


class buffer(Actor):
    def __init__(self):
        super().__init__()
        self._points = 1
        self.clear_buffer()
        position = Point(0, 0)
        self.set_position(position)

    def get_points(self):
        return self._points

    def clear_buffer(self):
        self.set_text("")
    
    def buffer_update(self, letter):
        #add the letter to buffer    
        self._text + letter
        self.set_text(self._text)
    
    def get_buffer(self):
        return self._text