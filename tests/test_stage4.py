import pytest
from range_expander import expand_ranges

def test_simple_range():
    assert expand_ranges("1-3") == [1, 2, 3]

def test_reversed_range():
    assert expand_ranges("5-3") == [5, 4, 3]

def test_single_point_range():
    assert expand_ranges("3-3") == [3]

def test_multiple_ranges_mixed():
    assert expand_ranges("1,4-6,8-6,3-3") == [1, 4, 5, 6, 8, 7, 6, 3]

def test_invalid_range_non_numeric():
    with pytest.raises(ValueError):
        expand_ranges("3-a")

def test_invalid_single_value():
    with pytest.raises(ValueError):
        expand_ranges("a")

def test_combination_with_invalid():
    with pytest.raises(ValueError):
        expand_ranges("1-3,5-b,7")

def test_spaces_and_valid_input():
    assert expand_ranges(" 2 - 4 , 6 ") == [2, 3, 4, 6]
