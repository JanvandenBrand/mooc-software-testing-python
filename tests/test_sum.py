import pytest
from src.sum import ListNode
from src.sum import TwoNumberSum


# test cases:
# example
# one list is longer than the other
# one list is null
# one list carries a 1 at the end

@pytest.mark.parametrize("list1, list2, result", 
    [
        pytest.param(
          [2, 4, 3], [5, 6, 4], [7, 0, 8],
          id="example"
        ),
        pytest.param(
            [0, 1], [0, 1, 2], [0, 2, 2],
            id="one list is longer"
        ),
        pytest.param(
            [], [0, 1], [0, 1],
            id="one list is null"
        ),
        pytest.param(
            [9, 9], [1], [0, 0, 1],
            id="one list carries a 1 at the end"
        )
    ]
)
def test_TwoNumberSum(list1, list2, result):
    expected = result
    l1 = ListNode(list1)
    l2 = ListNode(list2)
    sum = TwoNumberSum()
    actual = sum.addTwoNumbers(l1=l1, l2=l2)
    assert expected == actual
