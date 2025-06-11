class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Hash map 
        # track how many items {valude: times}
        # Time Complexity 
        count = {}
        for i, v in enumerate(nums):
            if v in count: 
                return True
            else:
                count[v] = 1 
        return False
            

        