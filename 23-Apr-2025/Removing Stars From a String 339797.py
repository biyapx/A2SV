# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
                
        return ''.join(stack)