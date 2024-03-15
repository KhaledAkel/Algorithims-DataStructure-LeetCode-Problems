class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        merged = []
        
        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval does not overlap with the previous, append it.
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # If the current interval overlaps with the previous one, merge them.
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
