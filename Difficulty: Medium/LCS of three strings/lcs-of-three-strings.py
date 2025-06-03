class Solution:
    def lcsOf3(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        dp = [[[0]*(l3+1) for _ in range(l2+1)] for __ in range(l1+1)]
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                for k in range(1, l3+1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(
                            dp[i-1][j][k],
                            dp[i][j-1][k],
                            dp[i][j][k-1]
                        )
        return dp[l1][l2][l3]