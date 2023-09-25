class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        start,i = 0,0

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]


        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if start == i-1:
                    output.append(str(nums[start]))
                else:
                    output.append(str(nums[start])+"->"+str(nums[i-1]))
                start = i

        if nums[start] == nums[-1]:
            output.append(str(nums[start]))
        else:
            output.append(str(nums[start])+"->"+str(nums[i]))


        return output
