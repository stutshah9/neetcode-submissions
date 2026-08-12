class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ""
        # create a hashmap to store each char and the count of each char
        charDict = defaultdict(int)
        for char in s:
            charDict[char] += 1

        # priorities the char with the highest count
        # use a min-heap for this but store values as negative so turns into a max heap
        min_heap = []
        for key, val in charDict.items():
            min_heap.append((-val, key))
        
        heapq.heapify(min_heap)
        previous = None

        while min_heap:
            # pop the most frequently available character
            count, char = heapq.heappop(min_heap)
            # add it to the result
            result += char
            # decrease its remaining count - must add because val is negative
            count += 1
            # put the PREVIOUS character back into the heap if it still has uses left
            if previous:
                heapq.heappush(min_heap, previous)
            # save the CURRENT character as the new previous character
            # if is still has a count
            if count < 0:
                previous = (count, char)
            else:
                previous = None
        
        if previous:
            return ""
        
        return result
