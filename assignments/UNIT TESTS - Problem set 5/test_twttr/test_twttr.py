import pytest
from twttr import shorten

def test_shorten_string():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TwIttEr") == "Twttr"

def test_shorten_not_string():
    with pytest.raises(TypeError):
        shorten(5)


def test_shorten_omitting_numbers():
    assert shorten("CS50") == "CS50"

def test_shorten_omitting_punctuation():
    assert shorten("CS50!") == "CS50!"