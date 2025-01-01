from bank import value

# Check Uppercase letters are converted
def test_case_sensitive():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("YOOO") == 100

# Check 0, 20 and 100 retured when their respective conditions are met
def test_0():
    assert value("hello") == 0

def test_20():
    assert value("hi") == 20

def test_100():
    assert value("yoo") == 100