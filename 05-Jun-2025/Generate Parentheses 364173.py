# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result

    def backtrack(self, result, current, open_count, close_count, n):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            self.backtrack(result, current + '(', open_count + 1, close_count, n)
        if close_count < open_count:
            self.backtrack(result, current + ')', open_count, close_count + 1, n)