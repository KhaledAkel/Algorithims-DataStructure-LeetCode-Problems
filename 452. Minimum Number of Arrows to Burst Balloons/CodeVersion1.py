class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        sorted_intervals = sorted(points, key=lambda point: point[1])
        current_end = sorted_intervals[0][1]
        arrows = 1

        for i in range(1, len(sorted_intervals)):
            new_start, new_end = sorted_intervals[i]
            if current_end < new_start:
                arrows += 1
                current_end = new_end

        return arrows
