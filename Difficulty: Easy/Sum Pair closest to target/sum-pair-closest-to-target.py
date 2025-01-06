class Solution:
    def sumClosest(self, arr, target):
        # Handle edge case where array has less than 2 elements
        if len(arr) < 2:
            return []
        
        # Sort the array
        arr.sort()
        
        left, right = 0, len(arr) - 1
        closest_diff = float('inf')  # To track the minimum difference
        closest_pair = []           # To store the pair with the closest sum
        
        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = abs(target - current_sum)
            
            # Update closest pair if current sum is closer to target
            if current_diff < closest_diff:
                closest_diff = current_diff
                closest_pair = [arr[left], arr[right]]
            elif current_diff == closest_diff:
                # Check for the pair with maximum absolute difference
                if abs(arr[right] - arr[left]) > abs(closest_pair[1] - closest_pair[0]):
                    closest_pair = [arr[left], arr[right]]
            
            # Move pointers based on comparison with target
            if current_sum < target:
                left += 1
            else:
                right -= 1
        
        return closest_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends