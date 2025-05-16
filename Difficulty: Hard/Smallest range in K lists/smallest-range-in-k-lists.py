import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])

        min_heap = []
        max_value = float('-inf')

        # Initialize heap with the first element from each list
        for i in range(k):
            heapq.heappush(min_heap, (arr[i][0], i, 0))  # (value, list_index, element_index)
            max_value = max(max_value, arr[i][0])

        range_start, range_end = -1e5, 1e5  # Some initial large range

        while True:
            min_value, list_idx, elem_idx = heapq.heappop(min_heap)

            # Update the range if it's smaller
            if max_value - min_value < range_end - range_start:
                range_start, range_end = min_value, max_value

            # Move to the next element in the same list
            if elem_idx + 1 < len(arr[list_idx]):
                next_elem = arr[list_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
                max_value = max(max_value, next_elem)
            else:
                break  # One list is exhausted

        return [range_start, range_end]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends