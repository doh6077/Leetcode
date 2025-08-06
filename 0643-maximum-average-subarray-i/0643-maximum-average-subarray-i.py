class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = 0 
        

        # First build window 
        for i in range(k):
            cur_sum += nums[i]
        largest = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i -k]
            largest = max(largest, cur_sum)
        
        return largest / k
        





        