from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_h():
    assert value("hey") == 20

def test_value_else():
    assert value("str") == 100
