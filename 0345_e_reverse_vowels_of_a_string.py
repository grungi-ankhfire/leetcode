class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s = list(s)
        l, r = 0, len(s)-1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while r > l and s[r] not in vowels:
                r -= 1
            
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
            
            l += 1
            r -= 1

    
        return "".join(s)


    def reverseVowels_naive(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        vow = []
        for c in s:
            if c.lower() in vowels:
                vow.append(c)
        
        res = ""
        for c in s:
            if c.lower() in vowels:
                res += vow.pop(-1)
            else:
                res += c
        return res

if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseVowels("IceCreAm") == "AceCreIm"
    assert solution.reverseVowels("leetcode") == "leotcede"
