class Solution:
    def canJump(self, nums: List[int]) -> bool:

        
        maxValue = 0 
        reach = len(nums) - 1
        for i in range(0, len(nums)):
            maxValue = max(nums[i] +  i, maxValue)
            if maxValue >= reach: return True
            if maxValue == i and nums[i] == 0:
                return False
            

        return False








