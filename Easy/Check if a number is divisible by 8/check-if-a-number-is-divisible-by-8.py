#User function Template for python3

class Solution:
    def DivisibleByEight(self, s):
        n = len(s)
        
        # If the length of the string is less than 3, check directly
        if n < 3:
            num = int(s)
            if num % 8 == 0:
                return 1
            else:
                return -1
        
        # Check the last three digits
        last_three = int(s[-3:])
        if last_three % 8 == 0:
            return 1
        else:
            return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends