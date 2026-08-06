class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):  
            # check if new start time is grater than old end time
            if newInterval[0] > intervals[i][1]:
            # append the old interval to the list
                result.append(intervals[i])
            # check if new end time is less than old start time
            elif newInterval[1] < intervals[i][0]:
            # append the new interval to the list
            # return the existing list + all the intervals in intervals from i onwards
                result.append(newInterval)
                return result + intervals[i:]
            # merge the 2 intervals together and have newInterval equal the merged interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)
        return result
