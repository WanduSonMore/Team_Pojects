# Description:
#   This section outputs what is changing while the code is running by using the data it recieves from the input, which it then send to the screen to change.
#  
# OOP Principles Used:
#   Abstraction and encapsulation
# Reasoning:
#   I believe that it uses abstraction because it uses a idea that if the user inputs this then this is what will change.
#   An example of this is whenever output recieves velocity points from input it will then use that velocity to move the player character.
#   This class used encapsulation because it put a underscore next to the sceens in this section which should help protect the assigned information.

import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering.""" 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)
        
    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7) # WHITE the number changes color based on 1 to 7

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.""" 
        self._screen.refresh()    