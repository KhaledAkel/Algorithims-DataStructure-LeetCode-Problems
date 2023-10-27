class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numsMap = {}
        occurSet = set()

        for num in arr:
            if num in numsMap.keys():
                numsMap[num] += 1
            else:
                numsMap[num] = 1

        for occur in numsMap.values():
            if occur in occurSet:
                return False
            else:
                occurSet.add(occur)
        return True 
        
