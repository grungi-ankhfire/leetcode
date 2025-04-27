from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is not None and self.val == other.val:
            return self.next == other.next
        return False


class Solution:
    carry = 0

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        val = self.carry
        self.carry = 0
        if val == 0 and self.carry == 0 and l1 is None and l2 is None:
            return None

        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next

        if val >= 10:
            val -= 10
            self.carry = 1

        return ListNode(val, self.addTwoNumbers(l1, l2))


if __name__ == "__main__":
    solution = Solution()

    list1_1 = ListNode(2, ListNode(4, ListNode(3)))
    list2_1 = ListNode(5, ListNode(6, ListNode(4)))
    result_1 = ListNode(7, ListNode(0, ListNode(8)))

    list1_2 = ListNode(0)
    list2_2 = ListNode(0)
    result_2 = ListNode(0)

    list1_3 = ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    )
    list2_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result_3 = ListNode(
        8,
        ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
            ),
        ),
    )

    assert solution.addTwoNumbers(list1_1, list2_1) == result_1
    assert solution.addTwoNumbers(list1_2, list2_2) == result_2
    assert solution.addTwoNumbers(list1_3, list2_3) == result_3
