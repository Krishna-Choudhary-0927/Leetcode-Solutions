class Solution:
    def mirrorDistance(self, n: int) -> int:
        n = str(n)
        rev_n = int(n[::-1])
        n = int(n)
        x = abs(n - rev_n)
        return x