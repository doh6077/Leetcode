class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_products = nums[0]
        # if size is 1, then return the only element 
        if len(nums) == 1:
            return max_products
    
        for i, num in enumerate(nums):
            if i ==1:
                continue
            temp_product = max_products * num
            if temp_product  > max_products:
                max_products = temp_products
            else:
                max_products = 1 

        return max_products
            
            

