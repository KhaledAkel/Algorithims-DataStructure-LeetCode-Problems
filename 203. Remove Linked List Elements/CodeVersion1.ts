/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeElements(head: ListNode | null, val: number): ListNode | null {
    // Create a dummy node to handle edge cases such as removing the head node
    let dummy = new ListNode(0, head);
    let current = dummy;

    // Traverse the list
    while (current.next !== null) {
        if (current.next.val === val) {
            // Skip the node with the given value
            current.next = current.next.next;
        } else {
            // Move to the next node
            current = current.next;
        }
    }

    // Return the new head of the list
    return dummy.next;
}
