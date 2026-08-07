class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            # not start of sequence
            if num - 1 in nums:
                continue

            curr_longest = 1
            curr_num = num
            while curr_num + 1 in nums:
                curr_longest += 1
                curr_num += 1
            longest = max(curr_longest, longest)

        return longest