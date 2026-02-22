from letterboxed import LetterBoxedSearchSpace

with open("words.scrabble.txt") as f:
    valid_words = [line.strip() for line in f]

puzzle = LetterBoxedSearchSpace(list("mkpzetuniach"), valid_words)

def test_constructor_creates_instance_variables():
    expected_game_letters = ['m', 'k',  'p','z', 'e', 't', 'u', 'n', 'i', 'a', 'c', 'h']
    expected_start_state = ('', None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    assert puzzle.game_letters == expected_game_letters, \
    "Expected " + expected_game_letters + ", got : " + str(puzzle.game_letters)
    assert puzzle.start_state == expected_start_state
    assert len(puzzle.valid_words) > 0
    assert 'skewness' in puzzle.valid_words

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


if __name__ == "__main__":
    test_constructor_creates_instance_variables()
    print("\n#1 LetterBoxedSearchSpace constructor passes!")
    
    test_is_final_state()
    print("\n#2 is_final_state passes!")

    print("\nAll tests passed!")