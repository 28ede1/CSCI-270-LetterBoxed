from search import SearchSpace, a_star_search
from math import *

class LetterBoxedSearchSpace(SearchSpace):

    def __init__(self, letters, words):
        """
        Search space representation for Letter Boxpuzzle.

        States include information about the current word built, the last letter clicked, and 
        a tuple that shows what game letters have been used.

        Ex:
        start_state = ('', None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        
        No word has been built yet, no letter has been clicked yet, and no letter has been used yet

        Args:
            letters (list[str]): list of board letters
            words (list[str]): complete list of all dictionary words sorted

        Attributes:
            self.game_letters (list[str]): the 12 game letters given
            self.valid_words (list[str]): the filtered valid dictionary words sorted
            self.start_state (tuple[int, int, tuple[int]]): represents starting game state information
        """
        super().__init__()
        self.game_letters = letters
        self.start_state = ('', None,  tuple([0] * len(letters)))
        self.valid_words = self.filter_out_invalid_words(words)

    def can_make_word_from_letters(self, word):
        for letter in word:
            if letter not in self.game_letters:
                return False
        return True
    
    def has_letters_on_same_edge(self, word):
            if len(word) == 1:
                return False
            left = 0
            right = 1

            while right < len(word):
                prev_char_index = self.game_letters.index(word[left])
                curr_char_index = self.game_letters.index(word[right])
                if prev_char_index // 3 == curr_char_index // 3:
                    return True
                left += 1
                right += 1
            return False

    def filter_out_invalid_words(self, word_list):
        """
        Based on game rules, filters out words that:

        1) contain characters that are not included in the list of 12 game letters
        2) containers any two adjacent characters that lie on the same 'edge' 

        Args:
            wordlist (list[str]) : list of all dictionary words sorted
        
        Return:
            filtered_list (list[str]) : list of all valid words 
        """

        filtered_words = []
        for word in word_list:
            if self.can_make_word_from_letters(word) and not self.has_letters_on_same_edge(word):
                filtered_words.append(word)
        return filtered_words

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
        """
        Use binary search to see if a target is in the filtered and sorted self.valid_words

        Args:
            target (str) : target word
        Return:
            (boolean) : True if found, False if not
        """
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
        """
        Use binary search to find whether or not 'prefix' string exist as some 
        prefix of a word in the self.valid_words sorted filtered list.

        Args:
            prefix (str) : prefix string

        Return:
           (boolean) : True is found/False if not found
        """
        left = 0
        right = len(self.valid_words) - 1
        prefix_length = len(prefix)

        while left <= right:
            mid = (right + left) // 2
            word_prefix = self.valid_words[mid][0:prefix_length]

            if word_prefix == prefix:
                return True
            elif word_prefix < prefix:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def does_not_lie_on_same_edge(self, prev_chosen_index, current_chosen_index):
        """
        Use mod to group game_letters into 4 rows and determine whether
        the letter at prev_chosen_index and letter at current_chosen_index
        lie in the same row/edge.

        Args:
            prev_chosen_index (int) : index of prev chosen letter
            current_chosen_index (int) : index of current letter to choose
        Return:
            (boolean) : False if they lie on the same edge, True if not
        """
        if prev_chosen_index is None: # to account for start state, any current_chosen_index is valid
            return True
        return not (prev_chosen_index // 3 == current_chosen_index // 3) # assumes there are 12 game letters in the game

    def get_successors(self, state):
        """
        Returns a list of tuples that reflected updated_game states.

        Args:
            state tuple(str, int, tuple(int)) : the current game state
        Return:
            successor_list tuple(tuple(str, int, tuple(int)), str, int)) : tuple consisting
            of new_state, action (letter chosen), and the cost associated with making the action.
            Cost is 1 if a 'ENTER' was pressed to make a new word, else cost is 0.
        """
        successor_list = []
        prev_letter_index = state[1]
        prev_word_built = state[0]
        letter_tracker = state[2]

        for i in range(len(self.game_letters)):
            if self.does_not_lie_on_same_edge(prev_letter_index, i) and self.is_prefix_of_valid_word(prev_word_built + self.game_letters[i]):

                # copy to avoid re-referencing
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
    """
    Heuristical function meant to score a state given a state and search space object.

    Args:
        letters list(str) : list of game letters
        words list(str) : list of dictionary words

    Return:
        heuristical function
    """

    def find_longest_unique_lettered_word_count(words):
        max_length = float("-inf")

        for word in words:
            max_length = max(max_length, len(set(word)))
        return max_length
    
    def find_least_used_letter_in_dictionary(game_letters, words):
        # assumes words is a filtered list of words
        freq_map = {}
        
        for letter in game_letters:
            freq_map[letter] = 0

        for word in words:
            for letter in word:
                if letter in freq_map:
                    freq_map[letter] += 1

        min_freq = float('inf')
        min_freq_letter = None

        for key in freq_map:
            if freq_map[key] < min_freq:
                min_freq = freq_map[key]
                min_freq_letter = key
        return game_letters.index(min_freq_letter)
            
    max_length_word = find_longest_unique_lettered_word_count(words)  

    def heuristic(state, space):
        """
        A score is assigned based on:

        1) given the longest unique letter word existing in words, and given the number of
        0s in the state, if game can be completed using 1 word, +1, if two words minimum are needed +2, if three words 
        +3, etc
        """

        # admissable
        state_score = 0
        state_0s_count = state[2].count(0)
        score = ceil(state_0s_count / max_length_word)
        state_score += score

        return state_score
    return heuristic