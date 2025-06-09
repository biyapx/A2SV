# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sub = [], []
        n = len(nums)

        def backtrack(i):

            #base case
            if i == n:
                res.append(sub[:])
                return

            #don't pick
            backtrack(i + 1)

            #pick
            sub.append(nums[i])
            backtrack(i + 1)
            sub.pop()

        backtrack(0)
        return res
