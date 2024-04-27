class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(steps):
            nonlocal count
            if steps < 0:
                return
            if steps == 0:
                count += 1
                return

            if steps in memo:
                count += memo[steps]
                return

            for i in range(1, 3):
                dfs(steps-i)

            memo[steps] = count

        count = 0 
        dfs(n)
        return count
