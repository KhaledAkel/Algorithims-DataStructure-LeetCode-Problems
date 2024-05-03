/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashMap = {};
    for (let i = 0; i<nums.length; i++){
        let diff = target - nums[i];
        if (hashMap[diff] !== undefined){
            return [hashMap[diff], i]
        };
        hashMap[nums[i]] = i;

    };
    
};
