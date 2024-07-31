# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Calculate the number of nodes
        nodes = 0
        temp = head
        while temp:
            nodes += 1
            temp = temp.next

        # Effective rotations needed
        k = k % nodes
        if k == 0:
            return head

        # Find the new head after (nodes - k) steps
        steps_to_new_head = nodes - k
        i = 0
        temp = head
        while i < (steps_to_new_head - 1):
            i += 1
            temp = temp.next

        # New head and new tail
        new_head = temp.next
        temp.next = None

        # Connect the end of the list to the original head
        end = new_head
        while end.next:
            end = end.next
        end.next = head

        return new_head
