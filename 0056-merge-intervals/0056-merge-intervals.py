class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Use two pointers, always compare two values in the boundary 
        result = []
        intervals = sorted(intervals)
        left, right = 0, 1 
        n = len(intervals)
        while left < right and right < n:
            if intervals[left][1] >= intervals[right][0] and intervals[left][1] >= intervals[right][1]:
                intervals[left] = [intervals[left][0], intervals[left][1]]
                
                del intervals[right]
                n = len(intervals)
                print(intervals)
            elif intervals[left][1] >= intervals[right][0] and intervals[left][1] < intervals[right][1]:
                intervals[left] = [intervals[left][0], intervals[right][1]]
                
                del intervals[right]
                n = len(intervals)
                print(intervals)
            else:
                left += 1 
                right += 1
                print(left, right)
        return intervals 




        