class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index=0, curr=[]):
            res.append(curr[:])

            for i in range(index, len(nums)):
                curr.append(nums[i])
                dfs(i+1, curr)
                curr.pop()
        dfs()
        return res
    

        
