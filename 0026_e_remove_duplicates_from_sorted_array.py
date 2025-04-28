from typing import List


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
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        for i, num in enumerate(nums, 1):
            if ptr == 0 or num != nums[ptr - 1]:
                nums[ptr] = num
                ptr += 1

        return ptr


def judge(solution: Solution, nums: List[int], expectedNums: List[int]) -> None:

    k: int = solution.removeDuplicates(nums)  # Calls your implementation

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]


if __name__ == "__main__":
    solution = Solution()

    judge(solution, [1, 1, 2], [1, 2])
    judge(solution, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
