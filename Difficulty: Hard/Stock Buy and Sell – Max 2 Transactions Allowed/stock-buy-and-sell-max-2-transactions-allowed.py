class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        first_buy = float('inf')
        first_profit = 0
        second_buy = float('inf')
        second_profit = 0

        for price in prices:
            first_buy = min(first_buy, price)   # Lowest price for first buy
            first_profit = max(first_profit, price - first_buy)  # Max profit from first transaction
            second_buy = min(second_buy, price - first_profit)  # Effective second buy price
            second_profit = max(second_profit, price - second_buy)  # Max profit from second transaction
        
        return second_profit


#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends