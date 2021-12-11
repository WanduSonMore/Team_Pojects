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
# from game.randomize_position import Randomize

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    # marquee = Actor()
    # marquee.set_text("")
    # marquee.set_position(Point(1, 0))
    # cast["marquee"] = [marquee]
    x5 = int(1)
    y5 = int(1)
    walls_left = []
    while y5 != 18:
        y5 = y5 + 1
        position = Point(x5, y5)
        wall_left = Actor()
        walls_left.append(wall_left)
        wall_left.set_text("|")
        wall_left.set_position(position)
    cast["wall_left"] = walls_left

    x5 = int(79)
    y5 = int(1)
    walls_right = []
    while y5 != 18:
        y5 = y5 + 1
        position = Point(x5, y5)
        wall_right = Actor()
        walls_right.append(wall_right)
        wall_right.set_text("|")
        wall_right.set_position(position)
    cast["wall_right"] = walls_right

    x = int(2)
    y = int(18)
    position = Point(x, y)
    wall_bottom = Actor()
    wall_bottom.set_text("_" * 77)
    wall_bottom.set_position(position)
    cast["wall_bottom"] = [wall_bottom]

    x = int(1)
    y = int(1)
    position = Point(x, y)
    wall_top = Actor()
    wall_top.set_text("_" * 79)
    wall_top.set_position(position)
    cast["wall_top"] = [wall_top]

    x4 = int(38)
    y4 = int(2)
    door = []
    while y4 != 5:
        if y4 == 2:
            position = Point(x4, y4)
            door_part = Actor()
            door.append(door_part)
            door_part.set_text("_____")
            door_part.set_position(position)
            y4 = y4 + 1
            x4 = x4 - 1
        elif y4 == 3:
            position = Point(x4, y4)
            door_part = Actor()
            door.append(door_part)
            door_part.set_text("| .|. |")
            door_part.set_position(position)
            y4 = y4 + 1
        else:
            position = Point(x4, y4)
            door_part = Actor()
            door.append(door_part)
            door_part.set_text("|__|__|")
            door_part.set_position(position)
            y4 = y4 + 1
        cast["door"] = door
    
    x = int(40)
    y = int(5)
    position = Point(x, y)
    great_button = Actor()
    great_button.set_text("0")
    great_button.set_position(position)
    cast["great_button"] = [great_button]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    blankey = Actor()
    blankey.set_text("o")
    blankey.set_position(position)
    cast["blankey"] = [blankey]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2 - 1)
    position = Point(x, y)
    old_al = Actor()
    old_al.set_text("QP")
    old_al.set_position(position)
    cast["old_al"] = [old_al]

    x = int(constants.MAX_X / 3)
    y = int(constants.MAX_Y / 3)
    position = Point(x, y)
    stan = Actor()
    stan.set_text(":)")
    stan.set_position(position)
    cast["stan"] = [stan]

    x = int(5)
    y = int(16)
    position = Point(x, y)
    zig = Actor()
    zig.set_text("A")
    zig.set_position(position)
    zig.set_value(int(0))
    cast["zig"] = [zig]

    x = int(7)
    y = int(16)
    position = Point(x, y)
    zag = Actor()
    zag.set_text("v")
    zag.set_position(position)
    zag.set_value(int(0))
    cast["zag"] = [zag]

    x = int(65)
    y = int(15)
    position = Point(x, y)
    polp = Actor()
    polp.set_text("pq")
    polp.set_position(position)
    polp.set_value(int(0))
    cast["polp"] = [polp]

    x = int(0)
    y = int(19)
    position = Point(x, y)
    text1 = Actor()
    text1.set_text("")
    text1.set_position(position)
    cast["text1"] = [text1]

    x = int(0)
    y = int(20)
    position = Point(x, y)
    text2 = Actor()
    text2.set_text("")
    text2.set_position(position)
    cast["text2"] = [text2]

    x2 = int(5)
    y2 = int(4)
    bushes = []
    while x2 != 12:
        if x2 == 5 and y2 == 4:
            position = Point(x2, y2)
            and_bushes = Actor()
            bushes.append(and_bushes)
            and_bushes.set_text("&")
            and_bushes.set_position(position)
            x2 = x2 + 6
        elif x2 == 11 and y2 == 4:
            position = Point(x2, y2)
            and_bushes = Actor()
            bushes.append(and_bushes)
            and_bushes.set_text("&")
            and_bushes.set_position(position)
            x2 = x2 - 6
            y2 = y2 + 3
        elif x2 == 5 and y2 == 7:
            position = Point(x2, y2)
            and_bushes = Actor()
            bushes.append(and_bushes)
            and_bushes.set_text("&")
            and_bushes.set_position(position)
            x2 = x2 + 6
        else:
            position = Point(x2, y2)
            and_bushes = Actor()
            bushes.append(and_bushes)
            and_bushes.set_text("&")
            and_bushes.set_position(position)
            x2 = x2 + 1
    cast["bushes"] = bushes

    x3 = int(65)
    y3 = int(13)
    buttons = []
    while y3 != 5:
        position = Point(x3, y3)
        button = Actor()
        buttons.append(button)
        button.set_text("O")
        button.set_position(position)
        y3 = y3 - 2
    cast["buttons"] = buttons

    x = int(0)
    y = int(0)
    position = Point(x, y)
    item_text = Actor()
    item_text.set_text("Keys: 0")
    item_text.set_position(position)
    cast["items"] = [item_text]
    
    berry_count = Actor()
    berry_count.set_value(int(0))
    cast["berry_count"] = [berry_count]

        
    a = int(0)
    key_list = []
    while a != 4:
        key_count = Actor()
        key_list.append(key_count)
        a += 1
    cast["key_count"] = key_list

    key_amount = Actor()
    cast["key_amount"] = [key_amount]




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
    script["update"] = [handle_collisions_action, move_actors_action] # randomize_position,
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)