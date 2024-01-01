class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = collections.defaultdict(int)
        k = 0

        for num in nums:
            if found[num] < 2:
                found[num] += 1
                nums[k] = num
                k += 1

        return k
