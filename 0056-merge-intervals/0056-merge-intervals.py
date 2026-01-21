class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # Use two pointers, always compare two values in the boundary 
        # intervals = sorted(intervals)
        # left, right = 0, 1 
        # n = len(intervals)
        # while left < right and right < n:
        #     if intervals[left][1] >= intervals[right][0] and intervals[left][1] >= intervals[right][1]:
        #         del intervals[right]
        #         n = len(intervals)
        #     elif intervals[left][1] >= intervals[right][0]:
        #         intervals[left] = [intervals[left][0], intervals[right][1]]        
        #         del intervals[right]
        #         n = len(intervals)
        #     else:
        #         left += 1 
        #         right += 1
        # return intervals 

        
        intervals.sort(key = lambda interval: interval[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # there is a overlap
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
            return merged 




        