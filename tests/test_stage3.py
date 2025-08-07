#test_stage3.py 
import pytest
from range_expander import expand_ranges

def test_basic_range_dash():
    assert expand_ranges("1-3") == [1, 2, 3]

def test_basic_range_double_dot():
    assert expand_ranges("4..6") == [4, 5, 6]

def test_basic_range_to():
    assert expand_ranges("10 to 12") == [10, 11, 12]

def test_basic_range_tilde():
    assert expand_ranges("7~9") == [7, 8, 9]

def test_mixed_input():
    assert expand_ranges("1,4..5,7 to 8,10~11,13-13") == [1, 4, 5, 7, 8, 10, 11, 13]

def test_invalid_input():
    with pytest.raises(ValueError):
        expand_ranges("1 to x")
