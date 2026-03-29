class Solution:
    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        
        # Edge cases
        if total_sum < diff or (total_sum + diff) % 2 != 0:
            return 0
        
        target = (total_sum + diff) // 2
        
        # DP array
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            # Traverse backwards for 0/1 knapsack
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[target]