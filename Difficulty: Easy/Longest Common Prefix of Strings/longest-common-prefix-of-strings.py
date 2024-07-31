class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        
        # Find the minimum length string
        min_length = min(len(s) for s in arr)
        
        # Start comparing characters
        prefix = ""
        for i in range(min_length):
            # Take the character from the first string as a reference
            char = arr[0][i]
            
            # Compare this character with the same position in other strings
            if all(s[i] == char for s in arr):
                prefix += char
            else:
                break
        
        return prefix if prefix else "-1"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends