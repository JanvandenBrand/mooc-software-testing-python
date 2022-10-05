import pytest
import sys
import os
sys.path.append(os.path.abspath("./src/"))
from chocolate_bags import calculate_bags


# Partition tests


def test_total_too_big(small=1, big=1, total=17, result=-1):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message


def test_only_big(small=1, big=3, total=10, result=0):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message


def test_big_and_small(small=5, big=3, total=17, result=2):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message


def test_only_small(small=5, big=2, total=3, result=3):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message


# parametrized tests
# pytest.mark.parametrize takes a string of parameters, 
# and a list of parameter values for the test function.
# Note that the function body does not change from above.
# This way you can run many tests automatically, 
# only varying the parameters for the partitions that you want to test
@pytest.mark.parametrize("small, big, total, result",
    [
        (1, 1, 17, -1), # Total is higher than small + big
        (1, 3, 10, 0), # Only big bags
        (5, 3, 17, 2), # Both big and small bags
        (5, 2, 3, 3), # Only small bags
    ]
)
def test_calculate_bags(small, big, total, result):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message


# Generate ID strings with the test data
# running pytest -v will show the test ID string
@pytest.mark.parametrize(
    "small, big, total, result",
    [
        pytest.param(
            1, 1, 17, -1,
            id="Total is higher than small + big"
        ),
        pytest.param(
            1, 3, 10, 0,
            id="Only big bags"
        ),
        pytest.param(
            5, 3, 17, 2,
            id="Both big and small bags"
        ),
        pytest.param(
            5, 2, 3, 3,
            id="Only small bags"
        ),
    ]
)
def test_calculate_bags_with_id(small, big, total, result):
    actual = calculate_bags(small, big, total)
    expected = result
    message = "Expected calculate_bags to returned {0}, but actual was {1}"\
        .format(expected, actual)
    assert actual == expected, message


# Boundary tests

