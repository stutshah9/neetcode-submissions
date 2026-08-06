class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach one pointer starting at the front the other at the back
        # an outer loop goes on while the front pointer is not greater than the back one
        # while the character for both the pointers is not a alphanumeric character move the pointers (front++ and back--)
        # if value of front pointer is not equal to value of back pointer return False
        # otherwise carry on untit front > back

        front = 0
        back = len(s) - 1

        while front < back:
            while not s[front].isalnum() and front < back:
                front += 1
            
            while not s[back].isalnum() and front < back:
                back -= 1
            
            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
        
        return True
            


