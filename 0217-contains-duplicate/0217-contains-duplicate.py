class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Hash map 
        # track how many items {valude: times}
        # Time Complexity 
        count = {}
        for i, v in enumerate(nums):
            if v in count: 
                count[v] += 1 
            else:
                count[v] = 1 
        for i in count.values():
            
            if i > 1:
                return True
        
        return False
            

        