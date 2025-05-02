from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        best = max(candies)
        return [x + extraCandies >= best for x in candies]

if __name__ == "__main__":
    solution = Solution()
 
    assert solution.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
    assert solution.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]
    assert solution.kidsWithCandies([12, 1, 12], 10) == [True, False, True]
