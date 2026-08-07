class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        starts_and_ends = {}
        ends_and_starts = {}

        for num in nums:
            prev = num - 1
            succ = num + 1
            start = ends_and_starts.get(num, num)
            end = starts_and_ends.get(num, num)

            if succ in starts_and_ends:
                end = starts_and_ends[succ]
                starts_and_ends.pop(succ)
            if prev in ends_and_starts:
                start = ends_and_starts[prev]
                ends_and_starts.pop(prev)

            starts_and_ends[start] = end
            ends_and_starts[end] = start
        
        longest = 1
        for start, end in starts_and_ends.items():
            length = end - start + 1
            if length > longest:
                longest = length
        
        return longest