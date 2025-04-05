# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        mx = 0

        for i in range(len(processorTime)):
            mx = max(mx, processorTime[i] + max(tasks[i*4: i*4 + 4]))
        return mx