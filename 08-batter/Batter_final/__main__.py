import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game.randomize_position import Randomize

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}
    _segments = []

    marquee = Actor()
    marquee.set_text("")
    marquee.set_position(Point(1, 0))
    cast["marquee"] = [marquee]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("==========")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    # # xr = int(x + 7)
    # # yr = int(y)
    # position = Point(x + 7, y)
    # robot2 = Actor()
    # robot2.set_text("#")
    # robot2.set_position(position)
    # cast["robot2"] = [robot2]

    x1 = int(30)
    y1 = int(10)
    position = Point(x1, y1)
    velocity = Point(1, 1)
    ball = Actor()
    ball.set_text("o")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]

    x2 = int(0)
    y2 = int(0)
    position = Point(x2, y2)
    wall_top = Actor()
    wall_top.set_text("_" * 80)
    wall_top.set_position(position)
    cast["wall_top"] = [wall_top]

    x3 = int(0)
    y3 = int(20)
    position = Point(x3, y3)
    wall_bottom = Actor()
    wall_bottom.set_text("^" * 80)
    wall_bottom.set_position(position)
    cast["wall_bottom"] = [wall_bottom]

    x4 = int(0)
    y4 = int(1)
    position = Point(x4, y4)
    wall_left = Actor()
    wall_left.set_text("|\n" * 19)
    wall_left.set_position(position)
    cast["wall_left"] = [wall_left]
    # position = Point(x4, y4)
    # wall_left = Actor()
    # wall_left.set_text("|" * 19)
    # wall_left.set_position(position)
    # cast["wall_left"] = [wall_left]

    
    x5 = int(79)
    y5 = int(0)
    walls = []
    while y5 != 19:
        y5 = y5 + 1
        position = Point(x5, y5)
        wall_right = Actor()
        walls.append(wall_right)
        wall_right.set_text("|")
        wall_right.set_position(position)
    cast["wall_right"] = walls

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("*")
            brick.set_position(position)
            cast["brick"].append(brick)


    # x6 = int(9)
    # y6 = int(4)
    # bricks = []
    # while y6 != 5:
    #     while x6 != 69 :
    #         x6 = x6 + 1
    #         position = Point(x6, y6)
    #         bricks_main = Actor()
    #         bricks.append(bricks_main)
    #         bricks_main.set_text("#")
    #         bricks_main.set_position(position)
    #     y6 = y6 + 1 
    # while y6 != 6:
    #     while x6 != 69 :
    #         x6 = x6 + 1
    #         position = Point(x6, y6)
    #         bricks_main = Actor()
    #         bricks.append(bricks_main)
    #         bricks_main.set_text("#")
    #         bricks_main.set_position(position)
    #     y6 = y6 + 1 
    # while y6 != 7:
    #     while x6 != 69 :
    #         x6 = x6 + 1
    #         position = Point(x6, y6)
    #         bricks_main = Actor()
    #         bricks.append(bricks_main)
    #         bricks_main.set_text("#")
    #         bricks_main.set_position(position)
    #     y6 = y6 + 1 
    # cast["bricks_main"] = bricks

        
    # artifacts = []
    # for n in range(constants.ARTIFACTS):
    #     text = chr(random.randint(33, 126))
    #     description = constants.MESSAGES[n]

    #     artifact = Actor()
    #     artifact.set_description(description)
    #     artifact.set_text(text)
    #     artifact.set_position(position)
    #     artifacts.append(artifact)
    # cast["artifact"] = artifacts

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    # randomize_position = Randomize()

    script["input"] = [control_actors_action]
    script["update"] = [handle_collisions_action, move_actors_action] #randomize_position,
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)

