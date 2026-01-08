class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        resMin, resMax = 1, 1

        for num in nums:
            temp = resMax* num
            resMax = max(resMax*num, resMin* num, num)
            resMin = min(resMin*num, temp, num)
            res = max(res, resMax)
        return res