"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Check if the input linked list is empty
        if not head:
            return None

        # Create the first node in the copied list
        copy = Node(head.val)
        copiedNodes = {head: copy}
        copyPointer = copy

        # Traverse the original linked list
        while head:
            # Check if the next node is already copied
            if head.next in copiedNodes:
                copyPointer.next = copiedNodes[head.next]
            else:
                # If not, create a new node and add it to the copied nodes dictionary
                if head.next == None:
                    copyPointer.next = None
                else:
                    copyPointer.next = Node(head.next.val)
                copiedNodes[head.next] = copyPointer.next

            # Check if the random node is already copied
            if head.random in copiedNodes:
                copyPointer.random = copiedNodes[head.random]
            else:
                # If not, create a new node and add it to the copied nodes dictionary
                if head.random == None:
                    copyPointer.random = None
                else:
                    copyPointer.random = Node(head.random.val)

                copiedNodes[head.random] = copyPointer.random

            # Move to the next nodes in the original and copied lists
            head = head.next
            copyPointer = copyPointer.next

        return copy




        
        
