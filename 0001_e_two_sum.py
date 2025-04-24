class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            visited[num] = i


if __name__ == "__main__":
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
