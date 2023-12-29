class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(node):
            visited.add(node)
            for city in range(len(isConnected)):
                if isConnected[node][city] == 1 and city not in visited:
                    dfs(city)
        provinces = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            provinces += 1
            dfs(i)
        return provinces
            

        
