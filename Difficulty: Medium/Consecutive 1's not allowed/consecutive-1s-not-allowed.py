class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        
        a = 2  # dp[1]
        b = 3  # dp[2]
        
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
            
        return b