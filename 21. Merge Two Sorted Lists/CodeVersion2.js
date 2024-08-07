/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let newList = new ListNode();
    let p = newList;

    while (list1 !== null || list2 !== null) {
        if (list1 === null) {
            p.next = new ListNode(list2.val);
            p = p.next;
            list2 = list2.next;
        } else if (list2 === null) {
            p.next = new ListNode(list1.val);
            p = p.next;
            list1 = list1.next;
        } else if (list1.val < list2.val) {
            p.next = new ListNode(list1.val);
            p = p.next;
            list1 = list1.next;
        } else {
            p.next = new ListNode(list2.val);
            p = p.next;
            list2 = list2.next;
        }
    }

    return newList.next;
    
};
