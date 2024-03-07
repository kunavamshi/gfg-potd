class Solution:
    def longestSubstring(self, s, n):
        # Create a 2D array to store the lengths of longest repeating non-overlapping substrings
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Initialize variables to store the maximum length and ending index of the substring
        max_length = 0
        end_index = 0
        
        # Iterate through the string to fill the dp array
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # If characters match and the substrings are non-overlapping, update dp[i][j] with dp[i-1][j-1] + 1
                if s[i - 1] == s[j - 1] and j - i > dp[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                    # Check if the current substring is longer than the maximum found so far
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        end_index = i
        
        # If no repeating non-overlapping substring is found, return -1
        if max_length == 0:
            return "-1"
        
        # Otherwise, return the longest repeating non-overlapping substring
        return s[end_index - max_length:end_index]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends