# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask = []
        
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a')) 
            bitmask.append((mask, len(word)))
        max_product = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if bitmask[i][0] & bitmask[j][0] == 0:
                    product = bitmask[i][1] * bitmask[j][1]
                    max_product = max(max_product, product)
                    
        return max_product