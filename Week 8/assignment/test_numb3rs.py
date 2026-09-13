from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("111.222.33.44") == True
    assert validate("199.242.333.44") == False
    assert validate("255.255.333.244") == False
    assert validate("255.22.1.256") == False