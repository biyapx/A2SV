# Problem: Insert a Node at the Tail of a Linked List - https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class Solution:
    def __init__(self, data, nxt):
        self.data = data 
        self.next = nxt
    def insertNodeAtTail(head, data):
        new_node = SinglyLinkedListNode(data)
        if head is None:
            return new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
            return head
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
