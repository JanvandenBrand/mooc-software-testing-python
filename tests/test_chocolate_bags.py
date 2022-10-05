import pytest
import sys
import os
sys.path.append(os.path.abspath("./src/"))
from chocolate_bags import calculate_bags


def test_total_too_big(small=5, big=3, total=17, result=2):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message
