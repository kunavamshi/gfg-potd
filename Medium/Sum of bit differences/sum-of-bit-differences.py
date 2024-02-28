class Solution:
    def sumBitDifferences(self, arr, n):
        total_bits = 0
        for i in range(32):  # assuming integers are represented using 32 bits
            count_0 = count_1 = 0
            for j in range(n):
                if (arr[j] & (1 << i)) == 0:
                    count_0 += 1
                else:
                    count_1 += 1
            total_bits += count_0 * count_1 * 2
        return total_bits

#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends