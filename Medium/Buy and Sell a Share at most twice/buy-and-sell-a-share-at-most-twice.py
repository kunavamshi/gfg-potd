from typing import List

class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        if n <= 1:
            return 0

        # Initialize arrays to store maximum profit in two transactions
        left_profit = [0] * n
        right_profit = [0] * n

        # Calculate maximum profit if selling on or before the ith day
        min_price = price[0]
        for i in range(1, n):
            min_price = min(min_price, price[i])
            left_profit[i] = max(left_profit[i - 1], price[i] - min_price)

        # Calculate maximum profit if buying on or after the ith day
        max_price = price[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, price[i])
            right_profit[i] = max(right_profit[i + 1], max_price - price[i])

        # Combine the left and right profits to get the maximum overall profit
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + right_profit[i])

        return max_profit


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends