from um import count


def test_count():
    assert count("um?") ==1
    assert count("Um, thanks") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy, though") == 0