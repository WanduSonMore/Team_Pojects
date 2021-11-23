class updater:
    def __init__(self):
        self.fail = 0
   
    def guess_check(self, guess, broken_chosen_word, lines):
        wrong = 0
        i = 0
        while i < len(broken_chosen_word):
                
                if guess == broken_chosen_word[i]:
                    lines[i] = guess
                    i += 1
                elif guess != broken_chosen_word[i]:
                    wrong += 1
                    i += 1
        if wrong != len(broken_chosen_word):
            return 'correct', lines, self.fail
        else:
            self.fail +=1
            return 'incorrect', lines, self.fail
     #check if it is a letter
        #check if it is contained in the word
        #if not in word, loop through
        #if not in word cut rope
    def can_play(self, lines):
        if self.fail != 4 and lines.count('_') != 0:
            return True
        else:
            return False

