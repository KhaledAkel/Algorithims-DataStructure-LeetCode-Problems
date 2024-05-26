class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
      
        new_head = head.next 
        temp = head
        
        while temp and temp.next:
            fast = temp.next.next  
            slow = temp.next 
            
            # Swap the pair
            slow.next = temp
            temp.next = fast
           
            if fast and fast.next:
                temp.next = fast.next  
            
            temp = fast  
        
        return new_head
