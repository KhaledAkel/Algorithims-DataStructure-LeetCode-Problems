class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        count=0
        for n in nums:
            if (n-1) not in numset:
                length=0
                while (n+length) in numset:
                    length+=1
                count=max(count,length)
        return count
