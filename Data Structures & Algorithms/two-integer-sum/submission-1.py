class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                complement_index = indices[complement]
                return [min(complement_index, i), max(complement_index, i)]
            indices[num] = i
        
        # fail
        return [-1, -1]