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
        zig = cast["zig"][0]
        zag = cast["zag"][0]
        polp = cast["polp"][0]
        item_text = cast["items"][0]
        bushes = cast["bushes"]
        button_1 = cast["buttons"][0]
        button_2 = cast["buttons"][1]
        button_3 = cast["buttons"][2]
        button_4 = cast["buttons"][3]
        key_1 = cast["key_count"][0]
        key_2 = cast["key_count"][1]
        key_3 = cast["key_count"][2]      
        keys = cast["key_amount"][0]
        berry_count = cast["berry_count"][0]
        great_button = cast["great_button"][0]

        for blankey in cast["blankey"]:

            # This is the beginning of the great button collision section.
            if blankey.get_position().equals(great_button.get_position()):
                if keys.get_value() != 3:
                    text1.set_text("Great Door: ERROR! INSUFFICIENT NUMBER OF KEYS!")
                    text2.set_text("THREE KEYS ARE REQUIRED TO HAVE ACCESS!")
                else:
                    text1.set_text("Andrew Morris: Congratulations! You won Blankey's Key Quest.")
                    text2.set_text("Thank you for playing my game.")
            # This is the end of the great button collision section.

            # This is the beginning of Old Al's collision section.
            elif blankey.get_position().equals(old_al.get_position()) or (blankey.get_position().get_y() == old_al.get_position().get_y() and blankey.get_position().get_x() == old_al.get_position().get_x()+1):
                position = Point(int(blankey.get_position().get_x()), int(blankey.get_position().get_y()+1))
                blankey.set_position(position)
            elif (blankey.get_position().get_y() == old_al.get_position().get_y()+1 and blankey.get_position().get_x() == old_al.get_position().get_x()+1) or (blankey.get_position().get_y() == old_al.get_position().get_y()+1 and blankey.get_position().get_x() == old_al.get_position().get_x()):
                if keys.get_value() <= 2:
                    text1.set_text("Old Al: Hello Blankey, I heard you wanted to travel beyond the Great Door. Currently it is locked and three keys are")
                    text2.set_text("needed to open it. You should be able to get them from Stan :), Polp pq, and Zig A. Come back to me when you get them.")
                # elif keys.get_value() == 1:
                #     text1.set_text("Old Al: Good job Blanky you got the first key ")
                else:
                    text1.set_text("Old Al: Excellect work Blanky, you got the three keys you needed to open the Great Door. All you need to do to open it is")
                    text2.set_text("to stand on the button (0) in front of it and the door should open for you to pass through. Good luck on you travels.")
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
                    text1.set_text("Stan: Thanks for geting those anderberries for me.")
            # This is the end of Stan's collision section.
            
            # This is the beginning of Zig's section
            elif blankey.get_position().equals(zig.get_position()):
                position = Point(int(blankey.get_position().get_x()), int(blankey.get_position().get_y()+1))
                blankey.set_position(position)
            elif blankey.get_position().get_y() == zig.get_position().get_y()+1 and blankey.get_position().get_x() == zig.get_position().get_x():
                if key_2.get_claim() == False:
                    if zag.get_value() <= 4:
                        text1.set_text("Zig: Hey Old Al (QP) said you needed my key to open the big door. I'll give it to you if you")
                        text2.set_text("go play tag with Zag (v). Go tag him five times or more and I will give it to you.")
                    else:
                        text2.set_text("Here is the key you wanted.")
                        key_2.set_claim(True)
                        keys.set_value(int(keys.get_value() + 1))
                        item_text.set_text(f"Keys: {keys.get_value()}")
                else:
                    text1.set_text("Zig: Thanks for playing with zag.")
            # This is the end of Zig's section

            # This is the beginning of Zag's section
            elif blankey.get_position().equals(zag.get_position()):
                x = random.randint(7, 16)
                y = random.randint(12, 17)
                position = Point(x, y)
                zag.set_position(position)
                zag.set_value(zag.get_value() + 1)
            # This is the end of Zag's section

            # This is the beginning of Polp's section
            elif blankey.get_position().equals(polp.get_position()) or (blankey.get_position().get_y() == polp.get_position().get_y() and blankey.get_position().get_x() == polp.get_position().get_x()+1):
                position = Point(int(blankey.get_position().get_x()), int(blankey.get_position().get_y()+1))
                blankey.set_position(position)
            elif (blankey.get_position().get_y() == polp.get_position().get_y()+1 and blankey.get_position().get_x() == polp.get_position().get_x()+1) or (blankey.get_position().get_y() == polp.get_position().get_y()+1 and blankey.get_position().get_x() == polp.get_position().get_x()):
                if key_3.get_claim() == False:
                    if polp.get_value() <= 3:
                        text1.set_text("Polp: Hey Old Al (QP) said you needed my key to open the big door. I'll give it to you if you push my buttons (O) in the correct order.")
                        text2.set_text("The button will turn into X and make a boop sound on correct and say beep and reset when incorrect.")
                    else:
                        key_3.set_claim(True)
                        keys.set_value(int(keys.get_value() + 1))
                        item_text.set_text(f"Keys: {keys.get_value()}")
                        text2.set_text("Here is my key.")
                else: 
                    text1.set_text("Polp: Thanks for playing my game.")
            # This is the end of Polp's section

            # This is the beginning of the button section            
            elif blankey.get_position().equals(button_1.get_position()):
                if button_1.get_text() == "O":
                    if polp.get_value() == 2:
                        text1.set_text("boop")
                        button_1.set_text("X") 
                        polp.set_value(int(polp.get_value() + 1))
                    else:
                        text1.set_text("beep")
                        button_1.set_text("O")
                        button_2.set_text("O")
                        button_3.set_text("O")
                        button_4.set_text("O")
                        polp.set_value(int(0))
                else:
                    text1.set_text("boop")
            elif blankey.get_position().equals(button_2.get_position()):
                if button_2.get_text() == "O":
                    if polp.get_value() == 3:
                        text1.set_text("boop")
                        button_2.set_text("X") 
                        polp.set_value(int(polp.get_value() + 1))
                    else:
                        text1.set_text("beep")
                        button_1.set_text("O")
                        button_2.set_text("O")
                        button_3.set_text("O")
                        button_4.set_text("O")
                        polp.set_value(int(0))
                else:
                    text1.set_text("boop")
            elif blankey.get_position().equals(button_3.get_position()):
                if button_3.get_text() == "O":
                    if polp.get_value() == 0:
                        text1.set_text("boop")
                        button_3.set_text("X") 
                        polp.set_value(int(polp.get_value() + 1))
                    else:
                        text1.set_text("If you got this message something went wrong with the code.")
                else:
                    text1.set_text("boop")
                    text2.set_text(f"Number: {polp.get_value()}")
            elif blankey.get_position().equals(button_4.get_position()):
                if button_4.get_text() == "O":
                    if polp.get_value() == 1:
                        text1.set_text("boop")
                        button_4.set_text("X") 
                        polp.set_value(int(polp.get_value() + 1))
                    else:
                        text1.set_text("beep")
                        button_1.set_text("O")
                        button_2.set_text("O")
                        button_3.set_text("O")
                        button_4.set_text("O")
                        polp.set_value(int(0))
                else:
                    text1.set_text("boop")
            # This is the end of the button section   

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