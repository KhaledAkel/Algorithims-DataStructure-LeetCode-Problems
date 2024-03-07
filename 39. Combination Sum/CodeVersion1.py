class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        visited = set()
        res = []
        
        def unique(lst):
            freq = [0] * 150
            for num in lst:
                freq[num - 1] += 1
            return tuple(freq)
        
        def dfs(start, cur, curSum):
            if curSum > target:
                return 
            if curSum == target:
                if unique(cur) in visited:
                    return
                res.append(cur[:])
                visited.add(unique(cur))
                return 
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                curSum += candidates[i]
                dfs(i, cur, curSum)
                curSum -= candidates[i]
                cur.pop()
        
        dfs(0, [], 0)
        return res
