# Description:
#   This is the section is where the program recieves information from the user through the use of the WASD keys, where it then uses it to creat volocities to send to output.
#  
# OOP Principles Used:
#   Abstraction and encapsulation
# Reasoning:
#   This class uses abstraction because although we can see it doing it, it does send the velocity points to the output when you push the button.
#   This class used encapsulation because it put a underscore next to the keys and current in this section which should help protect the assigned information.

import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # w
        self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d
        self._current = Point(1,1)

        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction