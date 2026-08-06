class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            # get right digit
            right = x % 10
            # get left digit
            left = x // div

            if left != right:
                return False
            
            # chop right digit
            x = x % div
            # chop left digit
            x = x // 10

            div = div / 100
        return True