class Solution:
    def search(self, arr, key):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == key:
                return mid

            # Check if the left half is sorted
            if arr[low] <= arr[mid]:
                # Check if the key lies within the sorted left half
                if arr[low] <= key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if the key lies within the sorted right half
                if arr[mid] < key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends