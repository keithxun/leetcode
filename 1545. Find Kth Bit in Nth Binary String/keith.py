class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1
        middle = length // 2 + 1
        
        if k == middle:
            return "1"
        elif k < middle:
            return self.findKthBit(n - 1, k)
        else:
            # Mirror position
            mirrored = length - k + 1
            bit = self.findKthBit(n - 1, mirrored)
            return "1" if bit == "0" else "0"