# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)
        return result