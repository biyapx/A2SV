# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # to save index and value
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                resv, resi = stack.pop()
                res[resi] = i - resi
            stack.append([v, i])
        return res