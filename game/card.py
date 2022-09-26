from random import randint


class Card():
    """
    The Card class 
    """
    def __init__(self):
        """
        Initializes itself with the value to 0.
        """
        self.value = 0

    def next_card(self):
        """
        Get a new card of value between 1 and 13
        """
        self.value = randint(1, 13)