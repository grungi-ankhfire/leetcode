class Solution:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        value = 0
        i = 0
        prev = 0
        for i, char in enumerate(s):
            v = self.values[char]
            if i == len(s) - 1:
                value += v
            if i > 0:
                if prev >= v:
                    value += prev
                else:
                    value -= prev    
            prev = v

        return value


if __name__ == "__main__":
    solution = Solution()

    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
