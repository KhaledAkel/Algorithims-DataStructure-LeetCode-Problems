# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstSet = set()

        temp = headA
        while temp:
            firstSet.add(temp)
            temp = temp.next
        
        temp = headB
        while temp:
            if temp in firstSet:
                return temp
            
            temp = temp.next
        
        
            
        
