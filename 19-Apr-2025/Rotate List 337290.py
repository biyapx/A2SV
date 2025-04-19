# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Calculate the length of the list and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Compute the effective number of rotations
        k = k % length
        if k == 0:
            return head
        
        # Find the new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # The new head is the next node of new_tail
        new_head = new_tail.next
        
        # Break the list and form the rotated list
        new_tail.next = None
        tail.next = head
        
        return new_head