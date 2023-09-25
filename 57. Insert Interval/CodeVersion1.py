class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[-1]
        output = []
        inserted = False  # Flag to track if the new interval is inserted

        if len(intervals) == 0:
            return [newInterval]

        for interval in intervals:
            # If newInterval is inserted, simply append remaining intervals
            if inserted:
                output.append(interval)
            # If newInterval is not yet inserted
            else:
                # If current interval ends before newInterval starts, add the current interval as it is
                if interval[-1] < start:
                    output.append(interval)
                # If current interval starts after newInterval ends, insert newInterval and add the rest
                elif interval[0] > end:
                    output.append([start, end])
                    output.append(interval)
                    inserted = True
                else:
                    # If there's an overlap, update start and end accordingly
                    start = min(start, interval[0])
                    end = max(end, interval[-1])

        # If newInterval has not been inserted yet (i.e., it comes after all existing intervals),
        # add it at the end of the output list
        if not inserted:
            output.append([start, end])

        return output
