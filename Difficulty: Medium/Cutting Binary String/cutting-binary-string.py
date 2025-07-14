class Solution:
    def cuts(self, s):
        n = len(s)
        powers_of_5 = set()
        
        # Precompute powers of 5 in binary (up to 2^30)
        power = 1
        while power <= int('1' * 30, 2):  # max 30 bits
            powers_of_5.add(bin(power)[2:])
            power *= 5

        # Initialize DP array
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 0 cuts needed for empty string

        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub in powers_of_5 and sub[0] != '0':  # valid and no leading zero
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1