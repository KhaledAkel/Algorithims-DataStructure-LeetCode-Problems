"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([ele.start for ele in intervals]) # n + nlogn
        end = sorted([ele.end for ele in intervals]) # n + nlogn

        count, rooms = 0, 0
        s, e = 0, 0

        # 0 5 15
        # 10 20 40

        while s <= (len(intervals)-1) and e <= (len(intervals)-1): # n
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            rooms = max(rooms, count)
        
        return rooms



