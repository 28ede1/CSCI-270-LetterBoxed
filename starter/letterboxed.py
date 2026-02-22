from search import SearchSpace, a_star_search


class LetterBoxedSearchSpace(SearchSpace):

    def __init__(self, letters, words):
        """
        Search space representation for Letter Boxpuzzle.

        A 'state' should include information about the current word build, the last letter clicked, and 
        some way of describing which of the letters in the puzzle have been used. 

        Ex:
        start_state = ('', None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        No word has been built yet, no letter has been clicked yet, and no letter has been used yet

        Args:
            letters (list[str]): list of board letters
            words (list[str]): list of valid dictionary words

        Attributes:
            self.game_letters (list[str]): the 12 board letters given
            self.valid_words (list[str]): the valid dictionary words 
            self.start_state (tuple[int, int, tuple[int]]): represents starting game state information
        """
        super().__init__()
        self.game_letters = letters
        self.valid_words = words
        self.start_state = ('', None,  tuple([0] * len(letters)))

    def get_start_state(self):
        return self.start_state

    def is_final_state(self, state):
        """
        Returns true is all letters in 'state' have been used AND
        current_word so far has a length of 1.

        Args:
            state (tuple[int, int, tuple[int]]): the current game state
        """
        letter_tracker = state[2]
        current_word = state[0]
        return 0 not in letter_tracker and len(current_word) == 1

    def get_successors(self, state):
        pass


def create_heuristic(letters, words):
    pass
