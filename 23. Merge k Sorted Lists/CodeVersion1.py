# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out = []
        for lis in lists:
            temp = lis
            while temp:
                out.append(temp.val)
                temp = temp.next

        out.sort()
        head = ListNode()
        temp = head

        for node in out:
            temp.next = ListNode(node)
            temp = temp.next

        return head.next



