class Solution:
    def maxSum(self, arr):
        # Sort the array
        arr.sort()
        
        # Re-arrange elements in a zigzag pattern to maximize differences
        n = len(arr)
        zigzag_arr = []
        
        # Using two pointers approach to alternate between smallest and largest
        left, right = 0, n - 1
        while left <= right:
            if left == right:
                zigzag_arr.append(arr[left])
            else:
                zigzag_arr.append(arr[left])
                zigzag_arr.append(arr[right])
            left += 1
            right -= 1
        
        # Calculate the circular sum of absolute differences
        max_sum = 0
        for i in range(n):
            max_sum += abs(zigzag_arr[i] - zigzag_arr[(i + 1) % n])
        
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends