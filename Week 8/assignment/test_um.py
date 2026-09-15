from um import count

def test_count():
    assert count("Um, Thnanks") == 1
    assert count("Um, Thnanks, Um...") == 2
    assert count("Um, Thnanks, Ummm...") == 1
    assert count("Um, Thnanks, yummy...") == 1
    assert count("pUm, Thnanks, yummy...") == 0