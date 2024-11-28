class Solution:
    def myAtoi(self, s):
        # Step 1: Initialize variables
        i, n = 0, len(s)
        result, sign = 0, 1
        
        # Step 2: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 3: Check for a sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 4: Process digits and ignore non-digits
        while i < n and s[i].isdigit():
            result = result * 10 + (ord(s[i]) - ord('0'))
            # Step 5: Handle overflow
            if result > 2**31 - 1 and sign == 1:
                return 2**31 - 1
            elif result > 2**31 and sign == -1:
                return -2**31
            i += 1

        return result * sign


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends