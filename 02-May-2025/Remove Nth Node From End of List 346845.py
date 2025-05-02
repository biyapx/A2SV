# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur_len = head
        while cur_len:
            length += 1
            cur_len = cur_len.next
        index = length - n
        curr = head
        if n == length:
            return head.next
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head