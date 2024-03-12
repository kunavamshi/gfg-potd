class Solution:
    def countPairs(self, mat1, mat2, n, x):
        sz = n * n
        l, r = 0, sz - 1
        cnt = 0

        while l < sz and r >= 0:
            sum_val = mat1[l // n][l % n] + mat2[r // n][r % n]

            if sum_val == x:
                l += 1
                r -= 1
                cnt += 1
            elif sum_val > x:
                r -= 1
            else:
                l += 1

        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends