function maxSubArray(nums: number[]): number {
    let currSum: number = nums[0];
    let maxSum: number = nums[0];

    for (let i = 1; i < nums.length; i++) {
        currSum = Math.max(nums[i], currSum + nums[i]);
        maxSum = Math.max(maxSum, currSum);
    }

    return maxSum;
}
