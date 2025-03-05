#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)  # Sort words by length
        dp = {}  # Dictionary to store longest chain ending at each word
        longest_chain = 1  # Minimum chain length is 1 (single word)

        for word in words:
            dp[word] = 1  # Each word starts with a chain length of 1
            for i in range(len(word)):  # Try removing one character at a time
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:  # If the predecessor exists, update chain length
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            longest_chain = max(longest_chain, dp[word])  # Update max chain length
        
        return longest_chain



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends