# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        before = head
        totalNodes = 0

        # Count the total number of nodes in the list
        while before:
            totalNodes += 1
            before = before.next
        
        # Calculate the position of the node to be removed
        n = totalNodes - n

        # If the node to be removed is the head
        if n == 0:
            return head.next

        # Reset before to the head and move to the node before the one to be removed
        before = head
        after = head.next
        while n > 1:
            n -= 1
            before = before.next
            after = after.next

        # Remove the nth node
        before.next = after.next

        return head
