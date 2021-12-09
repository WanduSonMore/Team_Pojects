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
        pass
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        blankey = cast["blankey"][0]
        wall_left = cast["wall_left"][0]
        wall_right = cast["wall_right"][0]
        wall_bottom = cast["wall_bottom"][0]
        wall_top = cast["wall_top"][0]
        text1 = cast["text1"][0]
        text2 = cast["text2"][0]
        stan = cast["stan"][0]
        old_al = cast["old_al"][0]
        item_text = cast["items"][0]
        bushes = cast["bushes"]
        key_1 = cast["key_count"][0]
        keys = cast["key_amount"][0]
        berry_count = cast["berry_count"][0]

        for blankey in cast["blankey"]:

            # This is the beginning of Old Al's collision section.
            if blankey.get_position().equals(old_al.get_position()) or (blankey.get_position().get_y() == old_al.get_position().get_y() and blankey.get_position().get_x() == old_al.get_position().get_x()+1):
                position = Point(int(blankey.get_position().get_x()), int(blankey.get_position().get_y()+1))
                blankey.set_position(position)
            elif (blankey.get_position().get_y() == old_al.get_position().get_y()+1 and blankey.get_position().get_x() == old_al.get_position().get_x()+1) or (blankey.get_position().get_y() == old_al.get_position().get_y()+1 and blankey.get_position().get_x() == old_al.get_position().get_x()):
                text1.set_text("Old Al: Hello Blankey, I heard you wanted to travel beyond the Great Door. Currently it is locked and three keys are")
                text2.set_text("needed to open it. You should be able to get them from Stan :), Polp pq, and Zig A. Come back to me when you get them.")
            # This is the end of Old Al's collision section.
            
            # This is the beginning of Stan's collision section.
            elif blankey.get_position().equals(stan.get_position()) or (blankey.get_position().get_y() == stan.get_position().get_y() and blankey.get_position().get_x() == stan.get_position().get_x()+1):
                position = Point(int(blankey.get_position().get_x()), int(blankey.get_position().get_y()+1))
                blankey.set_position(position)
            elif (blankey.get_position().get_y() == stan.get_position().get_y()+1 and blankey.get_position().get_x() == stan.get_position().get_x()+1) or (blankey.get_position().get_y() == stan.get_position().get_y()+1 and blankey.get_position().get_x() == stan.get_position().get_x()):
                if key_1.get_claim() == False:
                    if berry_count.get_value() <= 3:
                        text1.set_text("Stan: Hey Old Al (QP) said you needed my key to open the big door. I'll give it to you if you get me")
                        text2.set_text("four or more anderberries from the & bushes. The & bush will turn into a when picked.")
                        item_text.set_text(f"Keys: {keys.get_value()} AnderBerries: {berry_count.get_value()}")
                    else:
                        key_1.set_claim(True)
                        keys.set_value(int(keys.get_value() + 1))
                        berry_count.set_value(int(0))
                        item_text.set_text(f"Keys: {keys.get_value()}")
                        text2.set_text("Here is the key.")
                else: 
                    text1.set_text("Thanks for geting those anderberries for me.")
            # This is the end of Stan's collision section.

            # This is the beginning of the wall collision sections
            elif blankey.get_position().get_x() == wall_left.get_position().get_x():
                velocity = Point(1, 0)
                blankey.set_velocity(velocity)
            elif blankey.get_position().get_x() == wall_right.get_position().get_x():
                velocity = Point(-1, 0)
                blankey.set_velocity(velocity)
            elif blankey.get_position().get_y() == wall_top.get_position().get_y():
                velocity = Point(0, 1)
                blankey.set_velocity(velocity)
            elif blankey.get_position().get_y() == wall_bottom.get_position().get_y():
                velocity = Point(0, -1)
                blankey.set_velocity(velocity)
            # This is the end of the wall collision sections

            else:
                text1.set_text("")
                text2.set_text("")
        for bush in bushes:
            if blankey.get_position().equals(bush.get_position()):
                if bush.get_text() == "&":
                    berry_count.set_value(int(berry_count.get_value() + 1))
                    item_text.set_text(f"Keys: {keys.get_value()} AnderBerries: {berry_count.get_value()}")
                    bush.set_text("a")
                else: 
                    text1.set_text("You got the anderberry from this bush.")




        # marquee = cast["marquee"][0] # there's only one
        # robot = cast["robot"][0] # there's only one
        # artifacts = cast["artifact"]
        # marquee.set_text("")
        # for artifact in artifacts:
        #     if robot.get_position().equals(artifact.get_position()):
        #         description = artifact.get_description()
        #         marquee.set_text(description) 