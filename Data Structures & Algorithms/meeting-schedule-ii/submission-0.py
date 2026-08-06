"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # what is the maximum number of overlapping meetings at any given poin in time
        start = []
        for i in intervals:
            start.append(i.start)
        start = sorted(start)
        
        end = []
        for i in intervals:
            end.append(i.end)
        end = sorted(end)
        
        startP = 0
        endP = 0
        maxCounter = 0
        counter = 0

        while startP < len(intervals):
            if start[startP] < end[endP]:
                counter += 1
                startP += 1
            else:
                counter -= 1
                endP += 1
            
            maxCounter = max(maxCounter, counter)

        return maxCounter