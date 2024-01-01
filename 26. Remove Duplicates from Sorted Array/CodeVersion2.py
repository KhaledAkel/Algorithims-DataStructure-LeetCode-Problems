class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = set()
        k = 0

        for num in nums:
            if num not in found:
                nums[k] = num
                found.add(num)
                k += 1
        return k

        
