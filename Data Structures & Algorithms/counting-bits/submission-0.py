class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        # loops through the numbers from 0 to n
        for i in range(n+1):
            number = i
            count = 0
            while number:
                if number & 1 == 1:
                    count += 1
                number = number >> 1
            results.append(count)
        
        return results


