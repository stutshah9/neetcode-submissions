class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            tempSubset = []
            for subset in subsets:
                # do not add num to subset
                tempSubset.append(subset)
                # add number to subset
                # concatenate the subset list and num and create a new list
                addNum = subset+[num]
                tempSubset.append(addNum)
            subsets = tempSubset
        return subsets
        
        
