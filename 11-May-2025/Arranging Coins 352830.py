# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
        
        while (i * (i + 1)) // 2 <= n:
            count += 1
            i += 1
            
        return count