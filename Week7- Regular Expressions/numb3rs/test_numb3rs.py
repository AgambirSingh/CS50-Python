from numb3rs import validate

def test_good():
    assert validate("1.100.156.255") == True

def test_bad():
    assert validate("1.2.2.256")== False
    assert validate("a.b.c.d") == False
    assert validate("cat") == False