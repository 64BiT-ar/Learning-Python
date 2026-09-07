# pip install pytest
# No need to write main, print statement, try-except blocks

import pytest
from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(0) == 0
#     assert square(-2) == 4
#     assert square(-3) == 9

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): # It should raise type error, if any str i.e"cat" is passed. and it raises so test is passed
        square("cat")