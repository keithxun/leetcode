class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        digits = 0
        temp = n

        while temp > 0:
            temp >>= 1
            digits += 1
        
        mask = (1 << digits) - 1
        return n ^ mask