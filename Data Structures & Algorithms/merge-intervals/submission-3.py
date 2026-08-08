class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals using start time in ascending order
        intervals.sort(key = lambda item: item[0])

        result = []
        counter = 0
        result.append(intervals[0])

        # loop through the sorted intervals
        for interval in intervals:
        # for each interval if the start time is after the start and before the end time of the previous interval
            if result[counter][0] <= interval[0] <= result[counter][1]:
        # merge the intervals together
                if result[counter][1] <= interval[1] and result[counter][0] <= interval[0]:
                    result[counter] = [result[counter][0], interval[1]]
                else:
                    result[counter] = [result[counter][0], result[counter][1]]
            else:
                result.append([interval[0], interval[1]])
                counter += 1
        return result
