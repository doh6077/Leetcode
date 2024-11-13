class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for index, item in enumerate(nums):
            dicts[item] = index
        
        for i in dicts:
            diff = target - i 
            if diff in dicts and dicts[i] != dicts[diff]:
                return [dicts[i], dicts[diff] ]


 
        