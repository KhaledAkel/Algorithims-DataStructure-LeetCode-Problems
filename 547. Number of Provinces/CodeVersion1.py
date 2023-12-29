
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        for i in range(len(isConnected)):
            graph[i] = []
            for j in range(len(isConnected[0])):
                if j != i and isConnected[i][j] == 1:
                    graph[i].append(j)

        visited = set()
        province = 0

        for i in range(len(isConnected)):
            if i not in visited:
                province += 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    visited.add(node)
                    for city in graph[node]:
                        if city not in visited:
                            stack.append(city)
        return province
