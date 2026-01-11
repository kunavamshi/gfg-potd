class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        bestLen = float('inf')
        bestStart = -1

        def solve(i, j):
            # find leftmost start index ending at i matching s2[0..j]
            while i >= 0 and j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1
            return i + 1 if j < 0 else -1

        for i in range(n):
            if s1[i] == s2[m - 1]:
                start = solve(i, m - 1)
                if start != -1:
                    length = i - start + 1
                    if length < bestLen:
                        bestLen = length
                        bestStart = start

        return "" if bestStart == -1 else s1[bestStart:bestStart + bestLen]