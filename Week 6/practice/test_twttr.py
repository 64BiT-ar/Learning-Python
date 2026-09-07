from twttr import shorten

def test_shorten_upper():
    assert shorten("ELEPHANT") == "LPHNT"
    assert shorten("BROWNIES") == "BRWNS"

def test_shorten_lower():
    assert shorten("elephant") == "lphnt"
    assert shorten("brownies") == "brwns"

def test_shorten_mix():
    assert shorten("Fox") == "Fx"
    assert shorten("Brownies") == "Brwns"