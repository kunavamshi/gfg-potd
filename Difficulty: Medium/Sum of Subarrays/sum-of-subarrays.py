class Solution:
    def subarraySum(self, arr):
        total_sum = 0
        n = len(arr)
        for i in range(n):
            total_sum += arr[i] * (i + 1) * (n - i)
        return total_sum