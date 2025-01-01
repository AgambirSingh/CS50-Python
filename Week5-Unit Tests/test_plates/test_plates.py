from plates import is_valid

#Check if first 2 letter are not numbers
def test_first_letters():
    assert is_valid('0ab213') == False
    assert is_valid('a01234') == False
    assert is_valid('ab1234') == True
    assert is_valid('12345') == False

#check the length
def test_length():
    assert is_valid("A") == False
    assert is_valid("Dammmmmmm") == False

# Check if numbers are in the middle eg.(CS50XP)
def test_num_placement():
    assert is_valid("50XP") == False
    assert is_valid("CS50XP") == False

# Check if numbers o start with '0'
def test_0():
    assert is_valid("CS05") == False

# Check for invalid characters (periods, spaces, punctuation)
def test_alphanumeric():
    assert is_valid(".CS@50") == False
    assert is_valid("Cs 50") == False