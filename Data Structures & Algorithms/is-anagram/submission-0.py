from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = defaultdict(int)
        t_letters = defaultdict(int)

        for letter in s:
            s_letters[letter] += 1
        
        for letter in t:
            t_letters[letter] += 1
        
        return s_letters == t_letters