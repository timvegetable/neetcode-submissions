from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for s in strs:
            counter = frozenset(Counter(s).items())
            if counter in groups:
                groups[counter].append(s)
            else:
                groups[counter] = [s]

        return list(groups.values())