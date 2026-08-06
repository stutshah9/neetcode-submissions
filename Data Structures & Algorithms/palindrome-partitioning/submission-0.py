class Solution:
    def isPali (self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        def dfs(s):
            if not s:
                result.append(partition.copy())
                return
            for i in range(len(s)):
                part = s[:i+1]
                if self.isPali(part):
                    partition.append(part)
                    dfs(s[i+1:])
                    partition.pop()
        dfs(s)
        return result