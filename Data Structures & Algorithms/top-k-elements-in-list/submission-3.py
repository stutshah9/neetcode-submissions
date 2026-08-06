import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key: num, value: count
        dict = defaultdict(int)

        for num in nums:
            dict[num] += 1
        
        min_heap = []
        
        for num in dict:
            if len(min_heap) < k:
                # push the tuple (count, num) into the heap
                heapq.heappush(min_heap, (dict[num], num))
            else:
                heapq.heappush(min_heap, (dict[num], num))
                heapq.heappop(min_heap)
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
        return result
