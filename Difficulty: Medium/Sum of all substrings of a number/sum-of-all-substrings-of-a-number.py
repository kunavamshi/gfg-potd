class Solution:
    def sumSubstrings(self, s):
        n = len(s)
        total_sum = 0
        prev = 0

        for i in range(n):
            num = int(s[i])
            curr = prev * 10 + num * (i + 1)
            total_sum += curr
            prev = curr

        return total_sum