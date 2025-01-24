class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = [] 
        if not nums:
            return result
        
        start = nums[0]
        for i in range(1, len(nums) + 1):  # Loop through the list of numbers
            if i == len(nums) or nums[i] != nums[i-1] + 1:  # Check if the sequence is broken
                if start == nums[i-1]:
                    result.append(str(start))  # Single number, no range
                else:
                    result.append(f"{start}->{nums[i-1]}")  # Range from start to the previous number
                if i < len(nums):
                    start = nums[i]  # Update start to the new number
        return result





        


        