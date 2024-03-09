class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index, cur, curSum):
            if curSum > target:
                return
            if curSum == target:
                res.append(cur[:])
                return
            i = index
            while i < len(candidates):
                cur.append(candidates[i])
                curSum += candidates[i]
                dfs(i+1, cur, curSum)
                cur.pop()
                curSum -= candidates[i]
                while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                    i += 1
                i += 1
        dfs(0, [], 0)
        return res
