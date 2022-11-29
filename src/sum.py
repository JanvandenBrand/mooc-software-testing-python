from typing import Optional

# Taken from https://leetcode.com/problems/add-two-numbers/solution/
class TwoNumberSum:
    def addTwoNumbers(self, l1: Optional[list], l2: Optional[list]) -> Optional[list]:
        """_summary_

        Args:
            l1 (Optional[ListNode]): _description_
            l2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        l1.reverse()
        l2.reverse()
        carry = 0
        result = []

        for i in range(max(len(l1), len(l2))):
            if i < len(l1):
                first_value = l1[i]
            else:
                first_value = 0
            if i < len(l2):
                second_value = l2[i]
            else:
                second_value = 0
            column_sum = first_value + second_value + carry
            carry = 0
            if column_sum >= 10:
                carry = 1
                column_sum -= 10
            result.append(column_sum)

        result.reverse()
        return result
