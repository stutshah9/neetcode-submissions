class Solution:
    def countBits(self, n: int) -> List[int]:
        # time complexity: O(nlogn)
        # space complexity: O(1)
        # results = []
        # # loops through the numbers from 0 to n
        # for i in range(n+1):
        #     number = i
        #     count = 0
        #     while number:
        #         if number & 1 == 1:
        #             count += 1
        #         number = number >> 1
        #     results.append(count)
        
        # return results

        # time complexity: O(n)
        # space complexity: O(n)
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        
        return dp


