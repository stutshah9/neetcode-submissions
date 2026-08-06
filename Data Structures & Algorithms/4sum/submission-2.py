class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        # for loop through the nums list
        # a starts at the first index
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
        # foor loop through the nums list again
            for b in range(a+1,len(nums)-2):
        # b starts at the index after a
        # 2 pointer for c and d
        # c starts after the b index
        # d starts at the end
                if b > a+1 and nums[b] == nums[b-1]:
                    continue

                c = b+1
                d = len(nums) - 1

                diff = target - (nums[a] + nums[b])
                while c < d:
                    if diff == nums[c] + nums[d]:
                        output.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -=1
                    elif diff < nums[c] + nums[d]:
                        d -= 1
                    else:
                        c += 1
        return output