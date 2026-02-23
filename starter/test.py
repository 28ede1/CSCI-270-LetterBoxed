from letterboxed import LetterBoxedSearchSpace, create_heuristic
from search import uniform_cost_search, a_star_search

with open("words.scrabble.txt") as f:
    valid_words = [line.strip() for line in f]

puzzle = LetterBoxedSearchSpace(list("mkpzetuniach"), valid_words)

def test_constructor_creates_instance_variables():
    expected_game_letters = ['m', 'k', 'p','z', 'e', 't', 'u', 'n', 'i', 'a', 'c', 'h']
    expected_start_state = ('', None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    assert puzzle.game_letters == expected_game_letters, \
    "Expected " + expected_game_letters + ", got : " + str(puzzle.game_letters)
    assert puzzle.start_state == expected_start_state
    assert len(puzzle.valid_words) > 0

    assert "aah" not in puzzle.valid_words
    assert "tuna" not in puzzle.valid_words

def test_is_final_state():
    state_1 = ('k', 1, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
    state_2 = ('k', 1, (1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1))
    state_3 = ('ka', 1, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

    assert puzzle.is_final_state(state_1) == True
    assert puzzle.is_final_state(state_2) == False
    assert puzzle.is_final_state(state_3) == False

def test_get_sucessors():
    state_1 = ('pan', 7, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0))

    expected_successor_list = [
        (('panp', 2, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'p', 0),
        (('pane', 4, (0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0)), 'e', 0),
        (('pant', 5, (0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0)), 't', 0),
        (('pana', 9, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'a', 0),
        (('panh', 11, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1)), 'h', 0),
        (('n', 7, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'ENTER', 1)
    ]

    assert puzzle.get_successors(state_1) == expected_successor_list

def test_is_valid_word():
    assert puzzle.is_valid_word('aah') == False
    assert puzzle.is_valid_word('zzz') == False
    assert puzzle.is_valid_word('') == False
    assert puzzle.is_valid_word('a') == False
    assert puzzle.is_valid_word('zzzzz') == False
    assert puzzle.is_valid_word('zombies') == False
    assert puzzle.is_valid_word('zzz') == False

def test_is_prefix_of_valid_word():
    assert puzzle.is_prefix_of_valid_word("") == True
    assert puzzle.is_prefix_of_valid_word("a") == True
    assert puzzle.is_prefix_of_valid_word("bungalow") == False
    assert puzzle.is_prefix_of_valid_word("aaaa") == False
    assert puzzle.is_prefix_of_valid_word("zip") == True
    assert puzzle.is_prefix_of_valid_word("aah") == False
    assert puzzle.is_prefix_of_valid_word("zymt") == False

def test_does_not_lie_on_same_edge():
    assert puzzle.does_not_lie_on_same_edge(0, 0) == False
    assert puzzle.does_not_lie_on_same_edge(0, 1) == False
    assert puzzle.does_not_lie_on_same_edge(0, 2) == False
    assert puzzle.does_not_lie_on_same_edge(0, 3) == True
    assert puzzle.does_not_lie_on_same_edge(0, 5) == True
    assert puzzle.does_not_lie_on_same_edge(11, 5) == True
    assert puzzle.does_not_lie_on_same_edge(11, 11) == False
    assert puzzle.does_not_lie_on_same_edge(5, 9) == True
    assert puzzle.does_not_lie_on_same_edge(None, 1) == True

def test_get_sucessors():
    state_1 = ('pa', 9, (0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0))
    expected_successors_1 = [
        (('pam', 0, (1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0)), 'm', 0),
        (('pap', 2, (0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0)), 'p', 0),
        (('pae', 4, (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0)), 'e', 0),
        (('pat', 5, (0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)), 't', 0),
        (('pan', 7, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'n', 0),
        (('pai', 8, (0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0)), 'i', 0),
    ]

    state_2 = ('pan', 7, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0))
    expected_successors_2 = [
        (('panp', 2, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'p', 0),
        (('pane', 4, (0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0)), 'e', 0),
        (('pant', 5, (0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0)), 't', 0),
        (('pana', 9, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'a', 0),
        (('panh', 11, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1)), 'h', 0),
        (('n', 7, (0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 'ENTER', 1)
    ]


    actual_successors_1 = puzzle.get_successors(state_1)
    actual_successors_2 = puzzle.get_successors(state_2)

    assert len(expected_successors_1) == len(actual_successors_1)
    assert actual_successors_1 == expected_successors_1
    assert len(expected_successors_2) == len(actual_successors_2)
    assert actual_successors_2 == expected_successors_2

def test_search_space():
    uniform_cost_search(puzzle, memoize=True)

def test_a_star_search():
    words = puzzle.valid_words
    game_letters = puzzle.game_letters

    solution = a_star_search(puzzle, create_heuristic(game_letters, words))
    return solution

if __name__ == "__main__":
    test_constructor_creates_instance_variables()
    print("\n#1 LetterBoxedSearchSpace constructor passes!")
    
    test_is_final_state()
    print("\n#2 is_final_state passes!")

    test_is_valid_word()
    print("\n#3 is_valid_word passes!")

    test_is_prefix_of_valid_word()
    print("\n#4 is_valid_prefix_of_word passes!")

    test_does_not_lie_on_same_edge()
    print("\n#5 does_not_lie_on_same_edge passes!")

    test_get_sucessors()
    print("\n#6 get_successors passes!")

    print("\nAll tests passed!")
    # test_search_space()

    test_a_star_search()
