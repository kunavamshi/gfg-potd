class Solution:
    def maxValue(self, arr):
        if not arr:
            return 0
        n = len(arr)
        if n == 1:
            return arr[0]
        
        # Helper function for standard House Robber problem
        def houseRobber(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        # Case 1: Exclude last house
        max1 = houseRobber(arr[:-1])
        
        # Case 2: Exclude first house
        max2 = houseRobber(arr[1:])
        
        return max(max1, max2)
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends