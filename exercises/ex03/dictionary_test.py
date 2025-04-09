"""Test the functions in dictionary.py"""

__author__: str = "730476994"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_use() -> None:
    """Test use case for invert function"""
    example: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(example) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_2() -> None:
    """Test another use case for invert function"""
    example: dict[str, str] = {"FL": "Miami", "CA": "LA", "NY": "Brooklyn"}
    assert invert(example) == {"Miami": "FL", "LA": "CA", "Brooklyn": "NY"}


def test_invert_edge() -> None:
    """Test edge case for invert function -- empty dictionary"""
    example: dict[str, str] = {}
    assert invert(example) == {}


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jenner", "kylie": "jenner"}
    invert(my_dictionary)


def test_count_use() -> None:
    """Test use case for count function"""
    fruits: list[str] = ["cherry", "apple", "banana", "apple", "pear"]
    assert count(fruits) == {"cherry": 1, "apple": 2, "banana": 1, "pear": 1}


def test_count_use_2() -> None:
    """Test another use case for count function"""
    ice_cream: list[str] = [
        "chocolate",
        "vanilla",
        "chocolate",
        "strawberry",
        "oreo",
        "oreo",
    ]
    assert count(ice_cream) == {
        "chocolate": 2,
        "vanilla": 1,
        "strawberry": 1,
        "oreo": 2,
    }


def test_count_edge() -> None:
    """Test edge case for count function -- empty input"""
    edge: list[str] = []
    assert count(edge) == {}


def test_favorite_color_use() -> None:
    """Test use case for favorite_color function"""
    assert favorite_color({"sara": "pink", "kate": "blue", "eliza": "pink"}) == "pink"


def test_favorite_color_use_2() -> None:
    """Test another use case for favorite_color function"""
    assert (
        favorite_color(
            {
                "baylee": "green",
                "josh": "red",
                "liz": "green",
                "soph": "red",
                "toni": "blue",
            }
        )
        == "green"
    )


def test_favorite_color_edge() -> None:
    """test edge case for favorite_color function -- empty dictionary"""
    assert favorite_color({}) == ""


def test_bin_len_use() -> None:
    """Test use case for bin_len function"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_2() -> None:
    """Test another use case for bin_len function"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge() -> None:
    """Test edge case for the bin_len function -- empty list"""
    assert bin_len([]) == {}
