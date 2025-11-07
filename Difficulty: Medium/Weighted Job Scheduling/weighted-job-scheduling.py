import bisect

class Solution:
    def maxProfit(self, jobs):
        # Step 1: Sort jobs by end time
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)
        
        # Step 2: Extract end times for binary search
        end_times = [job[1] for job in jobs]
        
        # Step 3: dp[i] = max profit until i-th job
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        for i in range(1, n):
            profit_incl = jobs[i][2]
            
            # Find last job that doesn’t overlap
            idx = bisect.bisect_right(end_times, jobs[i][0]) - 1
            if idx != -1:
                profit_incl += dp[idx]
            
            # Either take this job or skip it
            dp[i] = max(dp[i-1], profit_incl)
        
        return dp[-1]