class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}|{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        n = len(s)
        length_str = []
        
        while i < n:
            # read until | for length
            while s[i] != '|':
                length_str.append(s[i])
                i += 1
            # consume the |
            i += 1
            # take the actual string
            length = int("".join(length_str))
            out.append(s[i:i+length])
            i += length
            length_str = []
        
        return out