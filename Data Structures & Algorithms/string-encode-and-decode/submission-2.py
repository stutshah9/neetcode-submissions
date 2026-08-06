class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for str in strs:
            encoded.append(f"{len(str)}#{str}")
        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            decoded.append(s[j:j+length])
            i = j + length 
        return decoded

