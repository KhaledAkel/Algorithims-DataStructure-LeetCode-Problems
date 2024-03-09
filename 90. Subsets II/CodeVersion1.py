class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        duplicate = set()
        def freq(lis):
            freq = [0]*20
            for num in lis:
                freq[num+9] += 1
            return tuple(freq)

        def dfs(index, cur):
            if freq(cur) in duplicate:
                return
            res.append(cur[:])
            duplicate.add(freq(cur))

            for i in range(index, len(nums)):
                cur.append(nums[i])
                dfs(i+1, cur)
                cur.pop()
        dfs(0, [])
        return res


        
