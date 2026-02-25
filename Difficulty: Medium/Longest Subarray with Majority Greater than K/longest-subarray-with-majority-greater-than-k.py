class Solution:
    def longestSubarray(self, arr, k):
        prefix = 0
        first_occurrence = {0: -1}
        ans = 0

        for i, val in enumerate(arr):
            if val > k:
                prefix += 1
            else:
                prefix -= 1

            if prefix > 0:
                ans = i + 1
            else:
                if prefix - 1 in first_occurrence:
                    ans = max(ans, i - first_occurrence[prefix - 1])

            if prefix not in first_occurrence:
                first_occurrence[prefix] = i

        return ans