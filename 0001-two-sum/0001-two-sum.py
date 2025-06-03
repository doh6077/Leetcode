class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for l in range(0, len(nums) - 1):
            for r in range(l+1,len(nums)):
                if nums[l] + nums[r] == target:
                    result.extend([l,r])
            

        
        return result





