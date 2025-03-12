class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        
        prev2, prev1 = cost[0], cost[1]
        
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr
        
        return min(prev1, prev2)

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends