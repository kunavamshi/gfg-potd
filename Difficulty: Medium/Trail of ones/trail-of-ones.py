class Solution:
    def countConsec(self, n: int) -> int:
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        a[1] = b[1] = 1

        for i in range(2, n + 1):
            a[i] = a[i-1] + b[i-1]
            b[i] = a[i-1]
        
        valid = a[n] + b[n]
        total = 2 ** n
        return total - valid