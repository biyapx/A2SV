# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def search(left, right):
            if left >= right:
                return left
            mid = left + (right - left)//2
            if isBadVersion(mid):
                return search(left, mid)
            else:
                return search(mid+1, right)
        return search(1, n)