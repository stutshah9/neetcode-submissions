import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # loop through the nums array pushing each thing onto the min heap
        # if the size of the heap is greater than k pop an item off
        # this will automatically be the smallest item because it is a min heap
        # after looping though all the elements return the root of the heap
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappush(min_heap, num)
                heapq.heappop(min_heap)
        
        return min_heap[0]