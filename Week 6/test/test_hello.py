from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ahmed") == "hello, Ahmed"

# code test/__init__.py 
# Tells, treat this folder not as module but as package
# A package is a module or modules organised inside of a folder