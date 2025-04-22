from math import log, ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reversed = 0
        while x > reversed:
            reversed = 10 * reversed + x % 10
            x //= 10

        return reversed == x or reversed // 10 == x


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome(1000030001) == False
    assert solution.isPalindrome(1000110001) == True
    assert solution.isPalindrome(1000021) == False
    assert solution.isPalindrome(313) == True
    assert solution.isPalindrome(1001) == True
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False
