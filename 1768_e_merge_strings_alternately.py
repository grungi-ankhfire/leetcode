from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for c1, c2 in zip_longest(word1, word2, fillvalue=""):
            res += c1 + c2
        return res

        # Naive implementation

        # res = ""
        # for i in range(0, max(len(word1), len(word2))):
        #     if i < len(word1):
        #         res += word1[i]
        #     if i < len(word2):
        #         res += word2[i]
        # return res


if __name__ == "__main__":
    solution = Solution()

    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
