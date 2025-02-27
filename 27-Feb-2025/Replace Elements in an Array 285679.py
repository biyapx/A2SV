# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        value_to_index = {value: index for index, value in enumerate(nums)}
        
        for old_value, new_value in operations:
            if old_value in value_to_index:
                index = value_to_index[old_value]  
                nums[index] = new_value 
                value_to_index[new_value] = index
                del value_to_index[old_value]
                
        return nums