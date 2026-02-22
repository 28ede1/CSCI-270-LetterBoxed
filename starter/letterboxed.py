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
        successor_list = []

        """
        Take in a state variable state_1 = ('pa', 9, (0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0)
        Create a list of tuples that consist of (next_state, action, cost)
        To do so:

        For each index (letter) in state_1[2]:
                #1 check that the last letter used and the next letter to choose do 
                not lie on the same on the same
                #2 check that the chosen letter 'leads' to some word in valid_words (by 'leads' this means that the  
                word to now build is the prefix of some word in valid_words)

                if #1 and #2 apply, create a new state variable that reflects the letter being added and initialize a tuple
                (next_state, action, cost) to add to the returned list

                ? Handle case for pressing Enter to lock in a word
                ? Handle case of whether or not to have a cost of 1 or 0
        """
        return successor_list


def create_heuristic(letters, words):
    pass
