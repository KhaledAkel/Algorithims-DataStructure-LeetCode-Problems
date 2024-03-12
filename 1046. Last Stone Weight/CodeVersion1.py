class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x == y:
                continue

            heapq.heappush(max_heap, -abs(x-y))
        
        if len(max_heap) == 0:
            return 0
        return -max_heap[0]
        
