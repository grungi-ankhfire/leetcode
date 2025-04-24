class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = len(strs[0])
        for i in range(length):
            substring = strs[-1][:length-i]
            if all(s.startswith(substring) for s in strs):
                return substring
        return ""

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        prefix = ""
        for i in range(min([len(s) for s in strs])):
            if all([s[i] == strs[0][i] for s in strs]):
                prefix += strs[0][i]
            else:
                return prefix
        return prefix

    def longestCommonPrefix3(self, strs: list[str]) -> str:
        prefix = ""
        for i in range(min([len(s) for s in strs])):
            charset = set([s[i] for s in strs])
            if len(charset) > 1:
                return prefix
            prefix += charset.pop()
        return prefix


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(["cat", "cat", "cat"]) == "cat"
