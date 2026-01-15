class Solution:
    def missingNumber(self, nums: List[int]) -> int:


        n = len(nums)

        for num in range(0, n + 1):
            if num in nums:
                nums.remove(num)
            else:
                return num

        