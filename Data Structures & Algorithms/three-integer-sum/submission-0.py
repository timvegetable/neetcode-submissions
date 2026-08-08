class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        nums.sort()
        i = 0
        curr = nums[i]

        while i < n - 1 and curr <= 0:
            target = -curr
            j = i + 1
            k = n - 1
            while j < k:
                summed = nums[j] + nums[k]
                if summed < target:
                    j += 1
                elif summed > target:
                    k -= 1
                else:
                    results.append([curr, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
            i += 1
            curr = nums[i]
            while i < n - 1 and nums[i - 1] == curr:
                i += 1
                curr = nums[i]

        return results