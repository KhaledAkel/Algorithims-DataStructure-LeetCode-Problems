class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        HashMap = {}
        
        for i in nums:
            if i in HashMap.keys():
                HashMap[i] += 1
            else:
                HashMap[i] = 1

        pointer, k = 0, 0
        for i in HashMap.keys():
            if HashMap[i] > 2:
                for j in range(2):
                    nums[pointer] = i
                    pointer += 1
                
            else:
                for j in range(HashMap[i]):
                    nums[pointer] = i
                    pointer += 1

        return pointer

