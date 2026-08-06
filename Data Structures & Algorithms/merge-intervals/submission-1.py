class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # each time interval consists of a start time and end time
        # sort the intervals list by the start time
        # loop though each interval in the list
        # have a merged list
        # check if the last element in the merged list has overlapping intervals with the current item
        # if so update the end time of the last item in the merged list
        # otherwise add the item to the merged list
        
        intervals.sort(key=lambda interval: interval[0])    # sort by start
        # add first interval into the list
        mergedList = []

        for start, end in intervals:
            if mergedList and start <= mergedList[-1][1]:
                mergedList[-1][1] = max(mergedList[-1][1], end)
            else:
                mergedList.append([start, end])
        return mergedList