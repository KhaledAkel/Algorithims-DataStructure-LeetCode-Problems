/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k%nums.length
    let copy1 =nums.slice(-k); // 5 6 7
    let copy2 = nums.slice(0, nums.length -k); // 1 2 3 4
    let j = 0;

    for (let i=0; i<nums.length; i++){
        if (i<k){
            nums[i] = copy1[i];

        }else{
            nums[i] = copy2[j];
            j++;
        }
    }

    
};