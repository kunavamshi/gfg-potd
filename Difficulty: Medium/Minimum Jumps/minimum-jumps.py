class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If first element is 0, we can't move
        if n == 1:  
            return 0
        if arr[0] == 0:  
            return -1

        # Initialize variables
        jumps = 1  # At least one jump needed
        maxReach = arr[0]  # Max index we can reach
        steps = arr[0]  # Steps we can still take

        for i in range(1, n):
            # If we reach the end, return jumps count
            if i == n - 1:
                return jumps
            
            # Update maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step
            steps -= 1
            
            # If no steps left, we must jump
            if steps == 0:
                jumps += 1
                # If the current index is beyond maxReach, we can't reach the end
                if i >= maxReach:
                    return -1
                # Reset steps to the maximum reach from current position
                steps = maxReach - i  
        
        return -1  # If we exhaust the loop without reaching the last index

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends