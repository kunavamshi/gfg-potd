class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        
        # Create a difference array
        diff_map = {}
        max_len = 0
        pre_sum1 = 0
        pre_sum2 = 0

        for i in range(n):
            pre_sum1 += a1[i]
            pre_sum2 += a2[i]
            
            curr_diff = pre_sum1 - pre_sum2
            
            if curr_diff == 0:
                max_len = i + 1
            elif curr_diff in diff_map:
                max_len = max(max_len, i - diff_map[curr_diff])
            else:
                diff_map[curr_diff] = i

        return max_len