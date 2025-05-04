# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        maxx = 0
        while head:
            res.append(head.val)
            head = head.next
        left = 0
        right = len(res) - 1

        while left < right:
            maxx = max(maxx, res[left] + res[right])
            left += 1
            right -= 1
        return maxx