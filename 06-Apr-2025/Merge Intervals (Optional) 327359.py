# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged = res[-1]
            
            if current_interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                res.append(current_interval)
        
        return res