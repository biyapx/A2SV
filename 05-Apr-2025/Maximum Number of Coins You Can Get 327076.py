# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        k = n//3
        maxx = 0
        piles.sort(reverse=True)
        for i in range(0,n-k):
            if i % 2 == 1:
                maxx += piles[i]
        return maxx