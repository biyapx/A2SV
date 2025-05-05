# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        part = length // k
        rest = length % k
        
        res = []
        curr = head
        for i in range(k):
            part_head = curr
            
            current_part_size = part + (1 if i < rest else 0)
            
            for j in range(current_part_size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part_head = curr.next
                curr.next = None
                curr = next_part_head
            
            res.append(part_head)
        
        return res