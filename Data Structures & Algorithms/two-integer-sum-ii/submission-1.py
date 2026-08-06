class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have 2 pointers, 1 at the start of the array and 1 at the end
        i = 0
        j = len(numbers) - 1
        while i < j:
            # check the sum of the numbers at those 2 pointers
            sum = numbers[i] + numbers[j]
            # if the sum is too big, decrease the right pointer
            if sum > target:
                j -= 1
            # if the sum is too small, increase the left pointer
            if sum < target:
                i += 1
            # if the sum is equal to the target return the values of i and j
            if sum == target:
                return [i+1, j+1]