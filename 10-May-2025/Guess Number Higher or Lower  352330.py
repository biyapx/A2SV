# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def helper(start, end):
            mid = start + (end - start)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                return helper(start,mid-1)
            else:
                return helper(mid+1,end)
        return helper(1, n)
