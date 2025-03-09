# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]  
        for num in sorted(count.keys()):
            result.extend([num] * count[num])
        
        return result