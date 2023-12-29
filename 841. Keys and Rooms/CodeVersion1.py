
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {}

        for room in range(len(rooms)):
            graph[room] = rooms[room]

        def dfs(node, visited):
            if node in visited:
                return

            visited.add(node)

            if len(visited) == len(rooms):
                return True

            for room in graph[node]:
                if dfs(room, visited):
                    return True

            return False

        visited = set()
        return dfs(0, visited)
