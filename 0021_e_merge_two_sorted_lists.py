from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if self.val == other.val:
            return self.next == other.next
        return False

class Solution:

    def get_minimum_node(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        if node1 is None:
            return node2
        elif node2 is None:
            return node1
        else:
            return node1 if node1.val <= node2.val else node2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val <= list2.val:
                res = list1
                res.next = self.mergeTwoLists(list1.next, list2)
            else:
                res = list2
                res.next = self.mergeTwoLists(list1, list2.next)

            return res
        
        



if __name__ == "__main__":
    solution = Solution()

    list1_1 = ListNode(1, ListNode(2, ListNode(4)))
    list2_1 = ListNode(1, ListNode(3, ListNode(4)))
    result_1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

    list1_2 = None
    list2_2 = None
    result_2 = None

    list1_3 = None
    list2_3 = ListNode(0)
    result_3 = ListNode(0)

    assert solution.mergeTwoLists(list1_1, list2_1) == result_1
    assert solution.mergeTwoLists(list1_2, list2_2) == result_2
    assert solution.mergeTwoLists(list1_3, list2_3) == result_3
 