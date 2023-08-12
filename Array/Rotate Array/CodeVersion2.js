/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    // unshift splice 
    nums.unshift(... nums.splice(-(k%nums.length)))
    
};