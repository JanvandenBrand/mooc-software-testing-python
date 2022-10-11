import pytest
import sys
import os
sys.path.append(os.path.abspath("./src/"))
from blackjack import play


@pytest.mark.parametrize("left, right, result",
[
    pytest.param(
        30, 30, 0,
        id="Both left and right bust"
    ),
    pytest.param(
        21, 30, 21,
        id="Left wins"
    )
])
def test_play(left, right, result):
    expected = result
    actual = play(left, right)
    message = "Expected {0}, but play({1}, {2})\
        returned {3}".format(expected, left, right, actual)
    
    assert expected == actual, message

