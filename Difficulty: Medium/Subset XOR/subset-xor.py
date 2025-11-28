class Solution:
    def subsetXOR(self, n: int):
        # XOR from 1..n based on pattern
        if n % 4 == 0:
            full_xor = n
        elif n % 4 == 1:
            full_xor = 1
        elif n % 4 == 2:
            full_xor = n + 1
        else:
            full_xor = 0

        # If XOR already equals n → take all
        if full_xor == n:
            return list(range(1, n + 1))

        # Otherwise remove x
        x = full_xor ^ n
        ans = []
        for i in range(1, n + 1):
            if i != x:
                ans.append(i)
        return ans