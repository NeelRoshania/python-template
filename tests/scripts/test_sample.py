import pytest

# usage: pytest tests/scripts/test_sample.py

# object extracts all jobs found in joblist
def test_sample_1():

    # test outcome
    with pytest.raises(Exception):
        raise Exception('Test sample')