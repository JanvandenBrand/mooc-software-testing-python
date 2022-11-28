import pytest
import sys
import os
sys.path.append(os.path.abspath("./src/"))
from ghappy import ghappy

# We'll say that a lowercase 'g' in a string is "happy" 
# if there is another 'g' immediately to its left or right. 
# Return true if all the g's in the given string are happy.

# Partitions
# there is only one g - false
# there are two g's but separated - false
# there are two g's next to each other - true
# there are three g's next to each other - true
# there are two g's next to each other and a 3rd is not - false

# Boundaries
# String length is 1 g - false
# String length is 2 g - true
# String length is 3 with two continguent g's - true
# The g's are at the start of the string - true
# The g's are at the end of the string - true


@pytest.mark.parametrize("string, result", [
    pytest.param(
        "xxgxx", False,
        id="there is only one g"
    ),
    pytest.param(
        "xgxgx", False,
        id="there are two g's but separated"
    ),
    pytest.param(
        "xxggx", True,
        id="there are two g's next to each other"
    ),
    pytest.param(
        "xgggx", True,
        id="there are three g's next to each other"
    ),
    pytest.param(
        "xggxgx", False,
        id="there are two g's next to each other and a 3rd is not"
    ),
    pytest.param(
        "g", False,
        id="String length is 1 g"
    ),
    pytest.param(
        "gg", True,
        id="String length is 2 g"
    ),
    pytest.param(
        "xgg", True,
        id="String length is 3 with two continguent g's"
    ),
    pytest.param(
        "ggxxxx", True,
        id="The g's are at the start of the string"
    ), 
    pytest.param(
        "xxxgg", True,
        id="The g's are at the end of the string"
    )
])
def test_ghappy(string, result):
    actual = ghappy(string)
    expected = result
    message = "Expected {0}, but ghappy('{1}') returned {2})"\
        .format(expected, string, actual)
    assert expected == actual, message
