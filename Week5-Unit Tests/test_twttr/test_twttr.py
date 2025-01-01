from twttr import shorten

# Check vowel replacements and lowercase vowel replacement
def test_lower():
    assert shorten("hello agam") == "hll gm"

# Checks uppercase, numbers and puncuations
def test_upper():
    assert shorten("CS50 FUN.") == "CS50 FN."