from app import hello, bye


def test_hello():
    assert hello() == "Hello, world!!"


def test_bye():
    assert bye == "Bye!"