from letterboxed import LetterBoxedSearchSpace

with open("words.scrabble.txt") as f:
    valid_words = [line.strip() for line in f]

def test_constructor_creates_instance_variables():
    puzzle = LetterBoxedSearchSpace(list("mkpzetuniach"), valid_words)

    expected_game_letters = ['m', 'k',  'p','z', 'e', 't', 'u', 'n', 'i', 'a', 'c', 'h']
    expected_start_state = ('', None, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    assert puzzle.game_letters == expected_game_letters, \
    "Expected " + expected_game_letters + ", got : " + str(puzzle.game_letters)
    assert puzzle.start_state == expected_start_state
    assert len(puzzle.valid_words) > 0
    assert 'skewness' in puzzle.valid_words

def test_is_final_state():
    puzzle = LetterBoxedSearchSpace(list("mkpzetuniach"), valid_words)

    state_1 = ('k', 1, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
    state_2 = ('k', 1, (1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1))
    state_3 = ('ka', 1, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

    assert puzzle.is_final_state(state_1) == True
    assert puzzle.is_final_state(state_2) == False
    assert puzzle.is_final_state(state_3) == False


if __name__ == "__main__":
    test_constructor_creates_instance_variables()
    print("\n#1 LetterBoxedSearchSpace constructor passes!")
    
    test_is_final_state()
    print("\n#2 is_final_state passes!")

    print("\nAll tests passed!")