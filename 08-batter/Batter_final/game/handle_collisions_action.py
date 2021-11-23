import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # marquee = cast["marquee"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        wall_left = cast["wall_left"][0]
        wall_top = cast["wall_top"][0]
        walls = cast["wall_right"][0]
        wall_bottom = cast["wall_bottom"][0]
        ball = cast["ball"][0]
        bricks = cast["brick"]
        
        # marquee.set_text("")
        # for artifact in artifacts:
        for ball in cast["ball"]:
            if paddle.get_position().get_y()-1 == ball.get_position().get_y():
                min_x = paddle.get_position().get_x()
                mid_x1 = min_x + 4
                mid_x2 = min_x + 5
                mid_x3 = min_x + 9
                # mid_x4 = min_x + 10
                # max_x = min_x + 14
                if ball.get_position().get_x() >= min_x and ball.get_position().get_x() <= mid_x1:
                    velocity = Point(random.randint(-3, 0), -1) #ball.get_velocity().get_x()
                    ball.set_velocity(velocity)
                # elif ball.get_position().get_x() >= mid_x2 and ball.get_position().get_x() >= mid_x3:
                #     velocity = Point(0, -1)
                #     ball.set_velocity(velocity)
                elif ball.get_position().get_x() >= mid_x2 and ball.get_position().get_x() <= mid_x3:
                    velocity = Point(random.randint(0, 3), -1)
                    ball.set_velocity(velocity)
        
            elif wall_top.get_position().get_y()+1 == ball.get_position().get_y():
                velocity = Point(ball.get_velocity().get_x(), 1)
                ball.set_velocity(velocity)
            
            elif wall_left.get_position().get_x()+1 == ball.get_position().get_x():
                velocity = Point(1, ball.get_velocity().get_y())
                ball.set_velocity(velocity)
            
            elif walls.get_position().get_x()-1 == ball.get_position().get_x():
                velocity = Point(-1, ball.get_velocity().get_y())
                ball.set_velocity(velocity)
            
            elif wall_bottom.get_position().get_y()-1 == ball.get_position().get_y():
                velocity = Point(0, 0)
                ball.set_velocity(velocity)
                wall_bottom.set_text("Game Over")

        brick_num = 0
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                velocity = ball.get_velocity().reverse_y()
                ball.set_velocity(velocity)
            brick_num += 1

        for paddle in cast["paddle"]:
            if paddle.get_position().get_x() == wall_left.get_position().get_x() + 1:
                velocity = Point(1, 0)
                paddle.set_velocity(velocity)
            
            if paddle.get_position().get_x() + 9 == walls.get_position().get_x():
                velocity = Point(-1, 0)
                paddle.set_velocity(velocity)