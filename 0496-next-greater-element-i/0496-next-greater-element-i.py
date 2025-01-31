class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)
        temp_result = [-1] *  n 
        stack = [] 
        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                temp_result[stack.pop()] = nums2[i]
            stack.append(i)
        
        n1 = len(nums1)
        result = [-1] *  n1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    result[i] = temp_result[j]
        return result 