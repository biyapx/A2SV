# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head == None:
            return head
        elif head != None and head.next == None:
            if head.val == val:
                return None
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy
            while head != None:
                if head.val == val:
                    prev.next = head.next
                    head = prev
                prev = head
                head = head.next
            return dummy.next