class Solution:
    def twoSum(self, arr, target):
        # Create a set to store the elements we've seen so far
        seen = set()
        
        # Iterate through the array
        for num in arr:
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the seen set
            if complement in seen:
                return True
            
            # Add the current number to the seen set
            seen.add(num)
        
        # If no such pair is found
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends