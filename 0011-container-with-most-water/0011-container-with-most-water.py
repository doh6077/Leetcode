class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1 
        maxdif = 0 
        while l < len(height) and r > l:
            dif = min(height[l], height[r]) * ( r - l)
            maxdif = max(dif, maxdif)
            if height[l] > height[r]:
                r = r -1 
            else:
                l = l + 1
        return maxdif

        