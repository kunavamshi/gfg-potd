class Solution:
    def isSubSeq(self, s1, s2):
        # Pointers for both strings
        i, j = 0, 0
        n, m = len(s1), len(s2)

        # Traverse both strings
        while i < n and j < m:
            if s1[i] == s2[j]:
                i += 1  # move in s1 if characters match
            j += 1      # always move in s2

        # If we traversed the whole s1, it's a subsequence
        return i == n