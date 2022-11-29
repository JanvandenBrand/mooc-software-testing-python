import pytest
from src.sum import TwoNumberSum


# test cases:
# example
# one list is longer than the other
# one list is null
# one list carries a 1 at the end

@pytest.mark.parametrize("list1, list2, result", 
    [
        pytest.param(
          [3, 4, 2], [4, 6, 5], [8, 0, 7],
          id="example"
        ),
        pytest.param(
            [1, 0], [2, 1, 0], [2, 2, 0],
            id="one list is longer"
        ),
        pytest.param(
            [], [1, 0], [1, 0],
            id="one list is null"
        ),
        pytest.param(
            [9, 9], [1], [1, 0, 0],
            id="one list carries a 1 at the end"
        )
    ]
)
def test_TwoNumberSum(list1, list2, result):
    expected = result
    sum2num = TwoNumberSum()
    actual = sum2num.addTwoNumbers(l1=list1, l2=list2)
    assert expected == actual
