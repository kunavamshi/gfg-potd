class Solution:
    def removeDuplicates(self, s: str) -> str:
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                result.append(char)
                seen.add(char)
        return ''.join(result)
#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends