# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_white = float('inf') 
        count = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        min_white = min(min_white, count)
        
        for i in range(k, n):
            if blocks[i - k] == 'W':
                count -= 1
            if blocks[i] == 'W':
                count += 1
            min_white = min(min_white, count)
        
        return min_white