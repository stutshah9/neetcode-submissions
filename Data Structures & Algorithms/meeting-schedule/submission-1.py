"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # time complexity: O(nlogn)
        # space complexity: O(n)
        # start by sorting all the intervals by start time
        # if the start time of the next interval is smaller than the end time of the previous interval return false
        # else return true

        if len(intervals) == 0 or len(intervals) == 1:
            return True

        intervals.sort(key = lambda item: item.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        return True


