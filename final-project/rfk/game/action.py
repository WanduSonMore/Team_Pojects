# Description:
#   The responsibility of this class of objects is translate user input into some kind of intent.
#  
# OOP Principles Used:
#   Polymorphism 
# Reasoning:
#   This file uses polymorphism because it is the one method that is used to execute the differnt scenarios.

class Action:
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in subclass")