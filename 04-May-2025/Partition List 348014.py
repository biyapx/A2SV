# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x = ListNode(0)
        greater_than_x = ListNode(0)

        start = less_than_x
        mid = greater_than_x
        cur = head
        while cur:
            if cur.val < x:
                less_than_x.next = ListNode(cur.val)
                less_than_x = less_than_x.next
            else:
                greater_than_x.next = ListNode(cur.val)
                greater_than_x = greater_than_x.next
            cur = cur.next
        less_than_x.next = mid.next
        greater_than_x.next = None
        return start.next