import pytest
from project import identify_generation, clean_text

def test_identify_generation_gen_z():
    text = "This party is so lit and the vibe is amazing!"
    assert identify_generation(text) == "Gen Z"

def test_identify_generation_boomer():
    text = "That's a groovy tune, really far out!"
    assert identify_generation(text) == "Boomer"

def test_identify_generation_gen_alpha():
    text = "Yas queen, you totally slay!"
    assert identify_generation(text) == "Gen Alpha"

def test_identify_generation_unknown():
    text = "I love reading books and going for walks."
    assert identify_generation(text) == "Unknown Generation"

def test_clean_text_removes_special_characters():
    text = "Hello, World! This is a test."
    expected = "Hello World This is a test"
    assert clean_text(text) == expected

def test_clean_text_trims_spaces():
    text = "   Lots of spaces before and after   "
    expected = "Lots of spaces before and after"
    assert clean_text(text) == expected

def test_identify_generation_mixed_keywords():
    text = "This party is lit and groovy, no cap!"
    # Gen Z keywords: "lit", "no cap"
    # Boomer keywords: "groovy"
    # Gen Z has more keywords, so it should be identified
    assert identify_generation(text) == "Gen Z"

# Add more test cases as needed

if __name__ == "__main__":
    pytest.main()
