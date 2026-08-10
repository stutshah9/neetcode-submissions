class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = 0

        for pile in piles:
            maxPile = max(maxPile, pile)

        left = 1
        right = maxPile

        while left < right:
            mid = (right + left) // 2
            hours = self.totalHours(piles, mid)
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
    
    def totalHours(self, piles, mid) -> int:
        count = 0
        for pile in piles:
            count += math.ceil(pile / mid)
        
        return count
