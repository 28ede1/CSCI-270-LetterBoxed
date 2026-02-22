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

        Uses the tuple given in the 2th index that keeps track of which letters have been used.

        Args:
            state (tuple[int, int, tuple[int]]): the current game state
        """
        letter_tracker = state[2]
        current_word = state[0]
        return 0 not in letter_tracker and len(current_word) == 1

    def is_valid_word(self, target):
        left = 0
        right = len(self.valid_words) - 1

        while left <= right:
            mid = (right + left) // 2

            if self.valid_words[mid] == target:
                return True 
            
            elif self.valid_words[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False 

    def is_prefix_of_valid_word(self, prefix):
        left = 0
        right = len(self.valid_words) - 1
        prefix_length = len(prefix)

        while left <= right:
            mid = (right + left) // 2
            word_prefix = self.valid_words[mid][:prefix_length]

            if word_prefix == prefix:
                return True
            elif word_prefix < prefix:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def does_not_lie_on_same_edge(self, prev_chosen_index, current_chosen_index):
        return not (prev_chosen_index // 3 == current_chosen_index // 3) # assumes there are 12 game letters in the game

    def get_successors(self, state):
        successor_list = []
        prev_letter_index = state[1]
        prev_word_built = state[0]
        letter_tracker = state[2]

        for i in range(len(self.game_letters)):
            if self.does_not_lie_on_same_edge(prev_letter_index, i) and self.is_prefix_of_valid_word(prev_word_built + self.game_letters[i]):
                new_tracker = list(letter_tracker)
                new_tracker[i] = 1
                new_tracker = tuple(new_tracker)

                new_state = (prev_word_built + self.game_letters[i], i, new_tracker)
                successor = (new_state, self.game_letters[i], 0)
                successor_list.append(successor)

        if self.is_valid_word(prev_word_built):
            new_state = (prev_word_built[-1], prev_letter_index, letter_tracker)
            successor = (new_state, 'ENTER', 1)
            successor_list.append(successor)

        return successor_list


def create_heuristic(letters, words):
    pass
