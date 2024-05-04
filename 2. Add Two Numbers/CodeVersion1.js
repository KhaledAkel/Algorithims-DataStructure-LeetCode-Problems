/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let remain = 0;
    let sumList = new ListNode();
    let pointer = sumList;

    while (l1 !== null || l2 !== null) {
        let x = l1 ? l1.val : 0;
        let y = l2 ? l2.val : 0;
        let currSum = x + y + remain;

        pointer.val = currSum % 10;
        remain = Math.floor(currSum / 10);

        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;

        if (l1 || l2 || remain) {
            pointer.next = new ListNode();
            pointer = pointer.next;
        }
    }

    if (remain !== 0) {
        pointer.val = remain;
    } else {
        pointer = null;
    }

    return sumList;
};
