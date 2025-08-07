#test code for stage7 
from range_expander import expand_ranges

def test_output_as_list():
    assert expand_ranges("1-3", output_format="list") == [1, 2, 3]

def test_output_as_csv():
    assert expand_ranges("1-3", output_format="csv") == "1,2,3"

def test_output_as_set():
    assert expand_ranges("1-3", output_format="set") == {1, 2, 3}

def test_invalid_format():
    try:
        expand_ranges("1-3", output_format="invalid")
    except ValueError as e:
        assert "Invalid output_format" in str(e)
    else:
        assert False, "Expected ValueError for invalid format"
