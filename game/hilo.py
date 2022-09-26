from game.card import Card


class Hilo():
    def __init__(self):
        """
        Initializes the game.
        """
        self.card = Card()
        self.score = 300
        self.run = True
    
    def start(self):
        """
        Get the first card and begin the game
        """
        self.card.next_card()
        self.output()

    def input(self):
        """
        Get user's input to guess higher or lower value of the next card.
        """
        return input("Higher or lower? [h/l] ")

    def update(self):
        """
        Compare the previous and next cards. If the guess is correct user gets a score. If the guess is wrong, the user gets deducted points. If user gets to 0 points the game ends.
        """
        old_card = self.card.value
        guess = self.input()
        self.card.next_card()

        if guess == "h":
            if self.card.value > old_card:
                self.score += 100
            
            else:
                self.score -= 75
        
        elif guess == "l":
            if self.card.value < old_card:
                self.score += 100
            
            else:
                self.score -= 75

        if self.score <= 0:
            self.run = False
            print("Game over")

    def output(self):
        """
        Game loop
        """
        while self.run:
            print()
            print("The card is: {}".format(self.card.value))
            self.update()
            print("Next card was: {}".format(self.card.value))
            print("Your score is: {}".format(self.score))
            
            if input("Play again? [y/n] ") == "n":
                self.run = False