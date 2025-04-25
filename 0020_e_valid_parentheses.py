class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack or stack.pop(-1) != pairs[c]:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False 
    assert solution.isValid("([])") == True
    assert solution.isValid("]") == False
