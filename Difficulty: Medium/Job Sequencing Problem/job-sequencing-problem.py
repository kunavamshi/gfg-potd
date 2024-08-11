#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        
class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # Sort jobs based on descending order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Find the maximum deadline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Initialize a list for free slots
        slots = [-1] * max_deadline
        
        job_count = 0
        total_profit = 0
        
        # Iterate over each job in decreasing order of profit
        for job in Jobs:
            # Find a free slot for this job (starting from the last possible slot)
            for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
                if slots[j] == -1:
                    # Slot found
                    slots[j] = job.id
                    job_count += 1
                    total_profit += job.profit
                    break
        
        return job_count, total_profit

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends