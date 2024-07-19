#User function Template for python3
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

class Solution:
    def constructLowerArray(self, arr):
        # Step 1: Coordinate compression
        sorted_unique_arr = sorted(set(arr))
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique_arr)}
        
        # Step 2: Initialize Fenwick Tree
        fenwick_tree = FenwickTree(len(sorted_unique_arr))
        result = []
        
        # Step 3: Traverse from right to left
        for num in reversed(arr):
            rank = rank_map[num]
            # Query the count of elements smaller than the current element
            count_smaller = fenwick_tree.query(rank - 1)
            result.append(count_smaller)
            # Update the Fenwick Tree with the current element
            fenwick_tree.update(rank, 1)
        
        # Reverse the result to match the original order
        return result[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends