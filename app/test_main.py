from app.main import is_isogram


def test_check_is_isogram_str() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("") is True
