# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def list_to_linked_list(lst):
            if not lst:
                return None

            # Create the head node with the first value
            head = ListNode(lst[0])
            current = head

            # Iterate over the remaining values in the list
            for val in lst[1:]:
                # Create a new node for each value
                new_node = ListNode(val)
                # Link the new node to the current node
                current.next = new_node
                # Move the current pointer to the new node
                current = new_node

            return head


        reversedList = []
        while head != None:
            reversedList = [head.val] + reversedList
            head = head.next
        
        return list_to_linked_list(reversedList)





        
