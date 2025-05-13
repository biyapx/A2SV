# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, index) for index, (start, end) in enumerate(intervals))
        res = [-1] * len(intervals)

        for i, (start, end) in enumerate(intervals):
            idx = bisect.bisect_left(starts, (end,))
            if idx < len(starts):
                res[i] = starts[idx][1]

        return res