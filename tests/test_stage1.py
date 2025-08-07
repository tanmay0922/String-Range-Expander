import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from range_expander import expand_ranges


def test_basic_range_expansion():
    assert expand_ranges("1-3,5,7-9") == [1, 2, 3, 5, 7, 8, 9]

def test_single_number():
    assert expand_ranges("5") == [5]

def test_single_range():
    assert expand_ranges("2-4") == [2, 3, 4]
