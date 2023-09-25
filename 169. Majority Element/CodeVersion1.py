class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        HashMap = {}
        for i in nums:
            if i in HashMap.keys():
                HashMap[i] += 1
            if i not in HashMap.keys():
                HashMap[i] = 1
        
        for key in HashMap.keys():
            if HashMap[key] > len(nums)/2:
                return key
