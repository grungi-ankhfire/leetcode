class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        for i in range(min(l1, l2), 0, -1):
            prefix = str1[:i]

            if prefix == str2[:i] and l1 % i == 0 and l2 % i == 0:
                if str1 == prefix * (l1 // i) and str2 == prefix * (l2 // i):
                    return prefix

        return ""


if __name__ == "__main__":
    solution = Solution()

    assert solution.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert solution.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert solution.gcdOfStrings("LEET", "CODE") == ""
