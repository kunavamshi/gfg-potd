import heapq

class Solution:
    def nearlySorted(self, arr, k):
        # Create a min-heap for the first k+1 elements
        min_heap = arr[:k+1]
        heapq.heapify(min_heap)
        
        # Initialize index for the sorted array
        index = 0

        # Process elements from k+1 to end of the array
        for i in range(k + 1, len(arr)):
            # Extract the minimum element from the heap
            arr[index] = heapq.heappop(min_heap)
            index += 1
            # Add the current element to the heap
            heapq.heappush(min_heap, arr[i])

        # Extract remaining elements from the heap
        while min_heap:
            arr[index] = heapq.heappop(min_heap)
            index += 1


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        print("~")
        t -= 1
# } Driver Code Ends