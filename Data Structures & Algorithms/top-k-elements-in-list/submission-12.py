class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time complexity: O(nlogn)
        # space complexity: O(n)
        # the input is not necessarily sorted
        # loop through all the nums in the string
        # create a dictionary with the values of the num and the count
        # key = num
        # value = count
        # sort the values in the dictionary in descending order
        # add the first k to the result list

        # result = []
        # numDict = defaultdict(int)

        # for num in nums:
        #     numDict[num] += 1
        
        # sortedNumDict = dict(sorted(numDict.items(), key=lambda item: item[1], reverse=True))

        # print(sortedNumDict)

        # count = 1
        # for num in sortedNumDict:
        #     if count <= k:
        #         result.append(num)
        #         count += 1
        # return result

        # time complexity: O(n) --> outer loop runs n times inner loop does not run n times on ever iterations thats why for that part the complexity is O(n) + O(n) = O(2n) and not O(n^2)
        # space complexity: O(n) --> O(n) + O(n) + O(n) = O(3n) --> dictionary + buckets + result
        # use a bucket idea where there are buckets of frequency ranging from n to 0 --> n+1 buckets
        # start with the bucket which corresponds to frequency n and work downwards
        # add numbers to resule until there are k elements which have been collected
        result = []
        numDict = defaultdict(int)

        for num in nums:
            numDict[num] += 1

        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num in numDict:
            value = numDict[num]
            bucket[value].append(num)

        count = 0
        for i in range(n, -1, -1):
            if count < k:
                if bucket[i]:
                    value = bucket[i]
                    for j in range(len(bucket[i])):
                        result.append(value[j])
                        count += 1
            else:
                break
        
        return result
        
        