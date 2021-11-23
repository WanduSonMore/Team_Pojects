import random
from game.actor import Actor
from game.action import Action
from game import constants
from game.point import Point


class Randomize(Action):
    pass
    # def __init__(self):
    #     super().__init__()
    #     self._segments = []
    
    # def execute(self, cast):
    #     if random.randint(0, 100) != 100:
    #         return

    #     for ball in cast["ball"]:
    #         x = random.randint(0, constants.MAX_X - 1)
    #         y = random.randint(1, constants.MAX_Y - 1)
    #         position = Point(x, y)
    #         ball.set_position(position)

    # def _add_segment(self, text, position, velocity):
    #     """Adds a new segment to the snake using the given text, position and velocity.

    #     Args:
    #         self (Snake): An instance of snake.
    #         text (string): The segment's text.
    #         position (Point): The segment's position.
    #         velocity (Point): The segment's velocity.
    #     """
    #     wall_left = Actor()
    #     wall_left.set_text(text)
    #     wall_left.set_position(position)
    #     wall_left.set_velocity(velocity)
    #     self._segments.append(wall_left)
