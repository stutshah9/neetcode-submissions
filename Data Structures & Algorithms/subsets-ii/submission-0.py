class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # since we have duplicates in the list the best way to avoid them would probably be using a set
        # the list can be sorted
        # have a backtrackign method which checks every route and adds it to the set if it is unique
        # backtracking - add something, call backtrack, remove something
        
        subsetSet = set()
        res = []
        nums.sort()
    
        def backtrack(i, subset):
            # base case: at index out of range
            if i == len(nums):
                subsetSet.add(tuple(subset))
                return

            # include the number
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # exclude the number
            backtrack(i+1, subset)

        backtrack(0, [])
        for s in subsetSet:
            res.append(s)
        return res