# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()  # Create a dummy node to simplify the code
        current = mergedList  # Use a pointer to keep track of the current node in the merged list

        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next

        # If one of the lists is not empty, append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return mergedList.next  # Skip the dummy node to get the actual merged list
        
