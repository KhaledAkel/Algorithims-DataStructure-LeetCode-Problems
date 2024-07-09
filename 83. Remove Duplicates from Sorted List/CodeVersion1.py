class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        pt = head

        while pt.next:
            if pt.val == pt.next.val:
                pt.next = pt.next.next
            else:
                pt = pt.next
        
        return head
