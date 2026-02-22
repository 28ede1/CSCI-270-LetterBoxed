from search import SearchSpace, a_star_search


class LetterBoxedSearchSpace(SearchSpace):

    def __init__(self, letters, words):
        """
        Search space representation for Letter Boxpuzzle.

        A 'state' should include information about the current cre
        """
        super().__init__()
        self.letter_tracker = {}
        self.valid_words = words

        for i in range(len(letters)):
            self.letter_tracker[i] = (letters[i], 0)

    def get_start_state(self):
        pass

    def is_final_state(self, state):
        pass

    def get_successors(self, state):
        pass


def create_heuristic(letters, words):
    pass
