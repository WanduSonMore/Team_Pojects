
class console:
    def __init__(self):
        self.letters_guessed = []
    
    def show_letters(self, letter_guess):
        self.letters_guessed.append(letter_guess)

    def show_lines(self, lines):
        print(" ".join(lines))

    def jumper_show(self, fail, chosen_word):
        
        if fail == 0:
            print(" ___")
            print("/___\ ")
            print("\   / ")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
            print()
            print("^^^^^^^")
        elif fail == 1:
            print("/___\ ")
            print("\   / ")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
            print()
            print("^^^^^^^")
        elif fail == 2:
            print("\   / ")
            print(" \ / ")
            print("  0 ")
            print(" /|\ ")
            print(" / \ ")
            print()
            print("^^^^^^^")
        elif fail == 3:
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
            print()
            print("^^^^^^^")
        elif fail == 4:
            print("  x") 
            print(" /|\ ") 
            print(" / \ ")
            print()
            print("^^^^^^^")
            print("Fatality")
            print(f"The word was {chosen_word}")
        print('you have guessed', ", ".join(self.letters_guessed))
