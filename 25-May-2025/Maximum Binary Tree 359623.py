# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_val = max(nums)
        root = TreeNode(max_val)
        center = nums.index(max_val)
        
        root.left = self.constructMaximumBinaryTree(nums[:center])
        root.right = self.constructMaximumBinaryTree(nums[center + 1:])
        
        return root