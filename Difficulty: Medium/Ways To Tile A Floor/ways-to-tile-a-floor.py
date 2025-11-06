class Solution:
    def numberOfWays(self, n):
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # DP approach: same recurrence as Fibonacci
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b