class Solution:
    def square(self, n):
        sum = 0
        while n:
            digit = n%10
            n = n // 10
            sum += digit * digit
        return sum

    def isHappy(self, n: int) -> bool:
        slow = self.square(n)
        fast = self.square(n)

        while fast != 1 and self.square(fast) != 1:
            slow = self.square(slow)
            fast = self.square(fast)
            fast = self.square(fast)

            if slow == fast:
                return False
        return True