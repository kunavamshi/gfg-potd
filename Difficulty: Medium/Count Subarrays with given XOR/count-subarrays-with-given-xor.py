class Solution:
    def subarrayXor(self, arr, k):
        xor_map = {}
        count = 0
        current_xor = 0

        for num in arr:
            current_xor ^= num  # Update the current XOR
            
            # If current XOR is equal to k, increment count
            if current_xor == k:
                count += 1
            
            # Check if there is a prefix array with XOR that satisfies the condition
            if current_xor ^ k in xor_map:
                count += xor_map[current_xor ^ k]
            
            # Update the map with the current XOR
            if current_xor in xor_map:
                xor_map[current_xor] += 1
            else:
                xor_map[current_xor] = 1
        
        return count



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends