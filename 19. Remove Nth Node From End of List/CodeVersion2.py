# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalNodes = 0
        current = head

        # Count the total number of nodes in the list
        while current:
            totalNodes += 1
            current = current.next

        # Handle the case where we need to remove the head
        if totalNodes == n:
            return head.next

        # Reset current to the head and move to the node before the one to be removed
        current = head
        for _ in range(totalNodes - n - 1):
            current = current.next

        # Remove the nth node
        current.next = current.next.next

        return head
