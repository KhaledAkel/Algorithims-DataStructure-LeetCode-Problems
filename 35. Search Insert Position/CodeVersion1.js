/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function searchInsert(nums, target) {
    let l = 0;
    let r = nums.length;

    while (l < r) {
        let mid = Math.floor((l + r) / 2);

        if (nums[mid] < target) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }

    return l;
}
