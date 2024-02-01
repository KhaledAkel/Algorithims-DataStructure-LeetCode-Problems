
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remain = 0
        sumList = ListNode()
        pointer = sumList

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            currSum = x + y + remain

            pointer.val = currSum % 10
            remain = currSum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2 or remain:
                pointer.next = ListNode()
                pointer = pointer.next

        if remain != 0:
            pointer.val = remain
        else:
            pointer = None

        return sumList
