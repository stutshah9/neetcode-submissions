import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            # negate it because python only supports min heaps
            # the largest number becomes the smallest number
            nums[i] = -nums[i]
        
        # restructure the array in place
        heapq.heapify(nums)

        for _ in range(k-1):
            # pop all the items till before the kth value
            # index 0 to index k-2 (1st element to k-1th element)
            heapq.heappop(nums)
        # multiply by -1 to make the value positive again
        return -heapq.heappop(nums)