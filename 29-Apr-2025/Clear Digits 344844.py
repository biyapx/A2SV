# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        res = ""
        for i in range(len(s)):
            stack.append(s[i])
            if stack[-1].isdigit():
                stack.pop()
                stack.pop()
        for i in stack:
            res += i
        return res