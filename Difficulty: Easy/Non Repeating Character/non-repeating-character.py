class Solution:
    
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # Using a dictionary to count the occurrences of each character
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterating through the string again to find the first non-repeating character
        for char in s:
            if char_count[char] == 1:
                return char
        
        # If no non-repeating character is found, return '$'
        return '$'
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

        print("~")

# } Driver Code Ends