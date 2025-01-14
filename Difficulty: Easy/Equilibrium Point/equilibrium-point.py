class Solution:
    # Function to find the equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)  # Calculate the total sum of the array
        left_sum = 0          # Initialize left sum as 0

        for i in range(len(arr)):
            # Calculate the right sum for the current index
            right_sum = total_sum - left_sum - arr[i]

            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i  # Return the index of the equilibrium point

            # Update the left sum for the next iteration
            left_sum += arr[i]

        return -1  # Return -1 if no equilibrium point is found





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends