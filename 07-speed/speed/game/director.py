#
# Suggestions:
#   - The attributes score, buffer and words should all be private
#

from time import sleep
from game import constants
from game.score import Score
from buffer import buffer
from words import words

class Director:
    def __innit__(self, input_service, output_service):
        self.input_service = input_service
        self.output_service = output_service
        self.keep_playing = True
        self.score = Score()
        self.buffer = buffer()
        self.words = words()

    def start_game(self):
        while self.keep_playing:
            
            
            
            sleep(constants.FRAME_LENGTH)


    def get_inputs(self):
        typed = self.input_service.get_letter()
        if typed == "*":
            self.buffer.clear_buffer()
        self.buffer_update(typed)

    def do_updates(self):
        self.handle_word_typed()


    def handle_word_typed(self):
        letters_typed = self.buffer.get_buffer()
        if self.word_check(letters_typed):
            self.score.add_points()
            self.buffer.clear_buffer()
    
    def do_outputs(self):
        # output services needed a lot here
        self._output_service.clear_screen()
      #  self._output_service.draw_actor(self.word)
      #  need draw_actor things for all words
        self._output_service.draw_actor(self.score)
        self._outtut_service.draw_actor(self.buffer)
        self._output_service.draw_actors(self.words)
        self._output_service.flush_buffer()
        

        
