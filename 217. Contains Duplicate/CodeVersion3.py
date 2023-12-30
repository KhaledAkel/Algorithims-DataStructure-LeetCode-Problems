class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        SET = set()
        for a in nums:
            if a in SET:
                return True
            SET.add(a)
        return False
        
