#test file code for stage6 
import pytest
from range_expander import expand_ranges

def test_simple_overlap():
    assert expand_ranges("1-3,2-5") == [1, 2, 3, 4, 5]

def test_duplicate_range():
    assert expand_ranges("1-3,3-5") == [1, 2, 3, 4, 5]

def test_single_numbers_with_overlap():
    assert expand_ranges("1,2,3,2,4") == [1, 2, 3, 4]

def test_step_with_overlap():
    assert expand_ranges("1-10:2,2-5") == [1, 3, 5, 7, 9, 2, 4]

def test_descending_step_with_overlap():
    assert expand_ranges("10-1:3,5-7") == [10, 7, 4, 1, 5, 6]

def test_invalid_range():
    with pytest.raises(ValueError):
        expand_ranges("3-a")

def test_zero_step():
    with pytest.raises(ValueError):
        expand_ranges("1-5:0")
