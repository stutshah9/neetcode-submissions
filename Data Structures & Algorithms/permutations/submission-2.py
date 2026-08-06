class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        
        # go through each number in the list at a time
        for n in nums:
            newPerms = []
            # go through each existing permutation
            for p in perms:
                # add the number to each possible position in the permutation
                for i in range(len(p)+1):
                    # have to make a copy because more permutations will be made
                    pCopy = p.copy()
                    # insert the number into the permutation at the specific position
                    pCopy.insert(i, n)
                    # append the new permutation to the list
                    newPerms.append(pCopy)
            # the total permutations is the new list of permutations that were created
            perms = newPerms
        return perms