class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0 
        for number in nums:
            if pointer <2 or number > nums[pointer-2]:
                nums[pointer] = number
                pointer += 1
        return pointer


