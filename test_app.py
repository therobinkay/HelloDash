from main import get_greet


def test_get_greet():
    assert 'Hi, Joseph' == get_greet('Joseph')
