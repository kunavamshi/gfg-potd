class Solution:
    def countSubstring(self, s):
        from collections import Counter
        
        freq = Counter(s)
        count = 0
        
        for ch in freq:
            n = freq[ch]
            # for each character, count of substrings starting and ending with it = n * (n + 1) // 2
            count += (n * (n + 1)) // 2
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends