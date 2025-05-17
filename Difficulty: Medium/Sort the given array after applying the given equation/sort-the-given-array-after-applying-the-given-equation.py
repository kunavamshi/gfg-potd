class Solution:
    def sortArray(self, arr, A, B, C):
        def f(x):
            return A * x * x + B * x + C

        n = len(arr)
        res = [0] * n
        left, right = 0, n - 1
        idx = n - 1 if A >= 0 else 0

        while left <= right:
            left_val = f(arr[left])
            right_val = f(arr[right])
            if A >= 0:
                if left_val > right_val:
                    res[idx] = left_val
                    left += 1
                else:
                    res[idx] = right_val
                    right -= 1
                idx -= 1
            else:
                if left_val < right_val:
                    res[idx] = left_val
                    left += 1
                else:
                    res[idx] = right_val
                    right -= 1
                idx += 1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        a = int(input())
        b = int(input())
        c = int(input())

        ob = Solution()
        ans = ob.sortArray(arr, a, b, c)
        print(' '.join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends