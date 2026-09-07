from fuel import convert, gauge
import pytest

def test_E():
    assert gauge(1) == "E"


def test_F():
    assert gauge(99) == "F"

def test_Z():
    assert gauge(59) == "59%"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("4/8") == 50