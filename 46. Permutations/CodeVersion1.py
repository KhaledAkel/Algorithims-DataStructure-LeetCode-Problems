class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(curr, lis):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in lis:
                next_curr = curr + [num]  # Create a new list for the next permutation
                next_lis = lis[:]
                next_lis.remove(num)  # Remove the current number from the list
                dfs(next_curr, next_lis)
        
        dfs([], nums)
        return res
