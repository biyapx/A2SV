# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 1
        left = 0
        last_pair_index = -1
        
        for right in range(1, n):
            if s[right] == s[right - 1]:
                if last_pair_index != -1:
                    left = last_pair_index + 1
                last_pair_index = right - 1
            max_len = max(max_len, right - left + 1)
        
        return max_len