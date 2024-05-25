# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        p = newList

        while list1 or list2:
            if not list1:
                p.next = ListNode(list2.val)
                p = p.next
                list2 = list2.next
            elif not list2:
                p.next = ListNode(list1.val)
                p = p.next
                list1 = list1.next
            elif list1.val < list2.val:
                p.next = ListNode(list1.val)
                p = p.next
                list1 = list1.next
            else:
                p.next = ListNode(list2.val)
                p = p.next
                list2 = list2.next
                
        return newList.next
