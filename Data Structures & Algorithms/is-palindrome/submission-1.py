class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        end = len(s) - 1
        l = 0
        r = end

        while l < r:
            while not s[l].isalnum() and l < end:
                l += 1
            while not s[r].isalnum() and r > 0:
                r -= 1
            if l < r and s[l].casefold() != s[r].casefold():
                return False
            l += 1
            r -= 1
        
        return True