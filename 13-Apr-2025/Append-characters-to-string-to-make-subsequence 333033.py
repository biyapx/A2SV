# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        i = 0
        j=0
        
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1
        
        return n - j