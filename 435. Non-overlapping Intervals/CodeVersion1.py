class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda pair:pair[0])
        last = intervals[0][-1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last:
                count += 1
                last = min(last, intervals[i][-1])
            else:
                last = intervals[i][1]
        
        return count
        
