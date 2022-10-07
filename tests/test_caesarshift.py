import pytest
import sys
import os
sys.path.append(os.path.abspath("./src/"))
from caesarshift import (
    caesarshiftcipher,
    caesarshiftcipher_fixed
)

# Test cases
# letter shifts right between a and z: c shift +3 -> f
# letter shifts left between z and a: n shift -3 -> k
# letter shifts right past z: x shift +3 -> a
# letter shifts left past a: b shift -3 -> y
# boundaries:
# a - 1 -> z
# z + 1 -> a
# a + 25 -> z
# z - 25 -> a 
# zero shift


@pytest.mark.parametrize("message, shift, result",
    [
        pytest.param(
            'abc', 3, 'def',
            id="letter shifts right between a and z"
        ),
        pytest.param(
            'nop', -3, 'klm',
            id="letter shifts left between z and a"
        ),
        pytest.param(
            'xyz', 3, 'abc',
            id="letter shifts right past z"
        ),
        pytest.param(
            'abc', -3, 'xyz',
            id="letter shifts left past a"
        ),
        pytest.param(
            'abc', -1, 'zab',
            id="a out boundry"
        ),
        pytest.param(
            'xyz', +1, 'yza',
            id="z out boundry"
        ),
        pytest.param(
            'a', 25, 'z',
            id='a in boundry'
        ),
        pytest.param(
            'z', -25, 'a',
            id='z in boundry'
        ),
        pytest.param(
            'abc', 0, 'abc',
            id="zero shift"
        )
    ]
)
def test_caesarshiftcipher(message, shift, result):
    expected = result
    actual = caesarshiftcipher(message, shift)
    message = "Expected {0}, but caesarshiftcipher({1}, {2},\
        returned {3}".format(expected, message, shift, actual)
    assert expected == actual


@pytest.mark.parametrize("message, shift, result",
    [
        pytest.param(
            'abc', 3, 'def',
            id="letter shifts right between a and z"
        ),
        pytest.param(
            'nop', -3, 'klm',
            id="letter shifts left between z and a"
        ),
        pytest.param(
            'xyz', 3, 'abc',
            id="letter shifts right past z"
        ),
        pytest.param(
            'abc', -3, 'xyz',
            id="letter shifts left past a"
        ),
        pytest.param(
            'abc', -1, 'zab',
            id="a out boundry"
        ),
        pytest.param(
            'xyz', +1, 'yza',
            id="z out boundry"
        ),
        pytest.param(
            'a', 25, 'z',
            id='a in boundry'
        ),
        pytest.param(
            'z', -25, 'a',
            id='z in boundry'
        ),
        pytest.param(
            'abc', 0, 'abc',
            id="zero shift"
        )
    ]
)
def test_caesarshiftcipher_fixed(message, shift, result):
    expected = result
    actual = caesarshiftcipher_fixed(message, shift)
    message = "Expected {0}, but caesarshiftcipher({1}, {2},\
        returned {3}".format(expected, message, shift, actual)
    assert expected == actual
