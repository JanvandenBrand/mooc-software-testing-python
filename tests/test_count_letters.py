import pytest
from src.count_letters import count_letters

# Partitions:
# 1. Multiple words that do and not end with r or s
# 2. single words that does not end with r  
# 3. single words that does not end with s 
# 4. last letter of the sentence is an r or s 


@pytest.mark.parametrize("string, result", [
    pytest.param(
        "It is raining cats and dogs!", 3,
        id="Multiple words that do and not end with r or s"
    ),
    pytest.param(
        "bayou", 0,
        id="single words that does not end with r"
    ),
    pytest.param(
        "moth", 0,
        id="single words that does not end with s"
    ),
    pytest.param(
        "last letter", 1,
        id="last letter of the sentence is an r or s"
    )
])
def test_count_letters(string, result):
    expected = result
    actual = count_letters(string)
    message = "Expected {0}, but count_letters returned {1}".format(
        expected, actual
    )
    assert expected == actual, message
