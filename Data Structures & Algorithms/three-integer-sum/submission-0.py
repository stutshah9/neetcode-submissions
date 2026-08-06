class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        # rearrange so that: -num[i] = num[j] + num[k]
        # sort the nums list
        # loop through each number in the list
        # have a nexted for loop with 2 pointers
        nums.sort()
        for i in range(len(nums)):
            # skip duplicates, this works because the list is sorted
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # start after i and never reuse i
            front = i + 1
            back = len(nums) - 1

            while front < back:
                # -num[i] = num[j] + num[k]
                if -nums[i] == nums[front] + nums[back]:
                    # append to output if sum is 0
                    output.append([nums[i], nums[front], nums[back]])
                    # move the pointers up and down one
                    front += 1
                    back -= 1

                    while front < back and nums[front] == nums[front-1]:
                        front += 1

                    while front < back and nums[back] == nums[back+1]:
                        back -= 1
                
                elif -nums[i] < nums[front] + nums[back]:
                    back -= 1
                else:
                    front +=1

        return output
