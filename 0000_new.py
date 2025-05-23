class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res.reverse()
        res = " ".join(res)
        print(res)
        return res


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"
