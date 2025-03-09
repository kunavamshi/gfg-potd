class Solution:
    def countPS(self, s):
        def expandAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= 2:  # Consider substrings of length ≥ 2
                    count += 1
                left -= 1
                right += 1
            return count

        n = len(s)
        palindrome_count = 0
        
        for i in range(n):
            palindrome_count += expandAroundCenter(i, i)      # Odd-length
            palindrome_count += expandAroundCenter(i, i + 1)  # Even-length
        
        return palindrome_count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends