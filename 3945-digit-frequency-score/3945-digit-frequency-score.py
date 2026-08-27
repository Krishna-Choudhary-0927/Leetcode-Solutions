class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        a = str(n)
        y = 0
        freq_d = 0
        for d in range(10):
            freq_d = a.count(str(d))
            y += d * freq_d
        return y