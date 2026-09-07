from plates import is_valid

def test_letter():
    assert is_valid("AA234") == True
    assert is_valid("23AB") == False

def test_mid_num():
    assert is_valid("AA23AA") == False

def test_zero_num():
    assert is_valid("AA0123") == False
    assert is_valid("AA1023") == True

def test_punc():
    assert is_valid("AS@323") == False
    assert is_valid("AS_323_@!") == False
    assert is_valid("_A3_@!") == False

def test_len():
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("A1234567") == False
    assert is_valid("AM2345") == True