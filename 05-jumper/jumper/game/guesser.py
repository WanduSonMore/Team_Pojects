class guesser:
    def __init__(self):
        pass

    def user_first(self):
        first_guess = input("Please choose a letter: ")
        return first_guess
    def user(self, checked_guess):
        if checked_guess == 'correct':
            game_continue = input("Good Guess! Please choose another letter: ")
            return game_continue
        elif checked_guess == 'incorrect':
            try_again = input("Bad Luck! Please choose another letter: ")
            return try_again