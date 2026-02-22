from letterboxed import LetterBoxedSearchSpace

with open("words.scrabble.txt") as f:
    valid_words = [line.strip() for line in f]

def test_constructor_initializes_letter_tracker_correctly():
    puzzle = LetterBoxedSearchSpace(list("mkpzetuniach"), valid_words)

    expected_tracker = {
        0: ("m", 0),
        1: ("k", 0),
        2: ("p", 0),
        3: ("z", 0),
        4: ("e", 0),
        5: ("t", 0),
        6: ("u", 0),
        7: ("n", 0),
        8: ("i", 0),
        9: ("a", 0),
        10: ("c", 0),
        11: ("h", 0),
    }

    assert puzzle.letter_tracker == expected_tracker, \
        "Should correctly initialize letter_tracker with index-letter pairs"


def test_constructor_stores_valid_words():
    puzzle = LetterBoxedSearchSpace(list("mkpzetuniach"), valid_words)

    assert len(puzzle.valid_words) > 0, \
        "valid_words should not be empty."

    assert "aah" in puzzle.valid_words, \
        "'aah' should exist in the loaded Scrabble word dictionary."


if __name__ == "__main__":
    test_constructor_initializes_letter_tracker_correctly()
    print("✓ letter_tracker initialized correctly")

    test_constructor_stores_valid_words()
    print("✓ valid_words stored correctly")

    print("\nAll constructor tests passed.")