import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from range_expander import expand_ranges

def test_stage2_basic_ranges():
    assert expand_ranges("1-3") == [1, 2, 3]
    assert expand_ranges("2,4-5") == [2, 4, 5]
    assert expand_ranges("7-7,8") == [7, 8]
    assert expand_ranges("10-12,15") == [10, 11, 12, 15]
