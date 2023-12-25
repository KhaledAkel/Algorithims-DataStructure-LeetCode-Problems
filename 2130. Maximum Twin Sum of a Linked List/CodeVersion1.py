# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        ele = []
        maxSum = 0
        n = 0
        while head:
            ele.append(head.val)
            n += 1
            head = head.next

        for i in range(n//2):
            maxSum = max(maxSum, ele[i] + ele[(n-1-i)])

        return maxSum

        

        





        

        
