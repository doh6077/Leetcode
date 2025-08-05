
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two Pointers 
        for i, num1 in enumerate(nums):
            rest = target - num1
            for j, num2 in enumerate(nums):
                if num2 == rest and i != j:
                    print(f"{i} and {j} and {rest}")
                    return [i, j]

        