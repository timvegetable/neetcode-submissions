class Solution:
    @staticmethod
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = list()

        for s in strs:
            is_unique = True
            for group in groups:
                if Solution.is_anagram(s, group[0]):
                    group.append(s)
                    is_unique = False
            if is_unique:
                groups.append([s])

        return groups