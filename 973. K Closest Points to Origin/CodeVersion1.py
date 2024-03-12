class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for coord in points: #n
            x, y = coord[0], coord[1]
            dist = math.sqrt((x) ** 2 + (y) ** 2)
            heapq.heappush(min_heap, (dist, x, y))  # logn

        # --> nlogn

        result = []
        for _ in range(k): # k
            dist, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result
