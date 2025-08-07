from range_expander import expand_ranges

def test_step_forward():
    assert expand_ranges("1-10:2") == [1, 3, 5, 7, 9]

def test_step_reverse():
    assert expand_ranges("10-1:3") == [10, 7, 4, 1]

def test_step_single():
    assert expand_ranges("5-5:1") == [5]

def test_mixed_with_normal():
    assert expand_ranges("2,4-6,10-2:2") == [2, 4, 5, 6, 10, 8, 6, 4, 2]

def test_step_invalid_step_non_numeric():
    try:
        expand_ranges("1-5:a")
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_step_zero_step():
    try:
        expand_ranges("1-5:0")
        assert False, "Expected ValueError"
    except ValueError:
        pass
