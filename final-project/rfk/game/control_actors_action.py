# Description:
#   The responsibility of this class of objects is translate user input into some kind of intent.
#  
# OOP Principles Used:
#   Inheritance, polymorphism and encapsulation
# Reasoning:
#   This class uses inheritance because the class DrawActorsAction is inheriting things from the action file.
#   This file uses polymorphism because it is one of the scenarios the action file can perform in the code.
#   This class used encapsulation because it put a underscore next to the input_service in this section which should help protect the assigned information.

from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        blankey = cast["blankey"][0] # there's only one in the cast
        blankey.set_velocity(direction)        
