class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        # Step 1: Find the first element from the right which is smaller than its next element
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:  # If such an element is found
            # Step 2: Find the smallest element on the right of 'i' that is greater than arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1

            # Step 3: Swap the two elements
            arr[i], arr[j] = arr[j], arr[i]

        # Step 4: Reverse the elements to the right of 'i' to get the next permutation
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends