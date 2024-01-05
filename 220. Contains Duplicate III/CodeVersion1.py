class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        Map = {}

        for i in range(len(nums)):
            key = nums[i] // (valueDiff + 1)
            if key in Map:
                return True
            if key+1 in Map:
                if abs(Map[key+1] - nums[i]) <= valueDiff:
                    return True
            if key-1 in Map:
                if abs(Map[key-1] - nums[i]) <= valueDiff:
                    return True
            Map[key] = nums[i]

            if i >= indexDiff:
                del Map[nums[i-indexDiff] // (valueDiff+1)]
        return False
        
