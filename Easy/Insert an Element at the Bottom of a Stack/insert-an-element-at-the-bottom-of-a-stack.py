#User function Template for python3
class Solution:
    def insertAtBottom(self, st, x):
        temp_stack = []
        while st:
            temp_stack.append(st.pop())
        st.append(x)
        while temp_stack:
            st.append(temp_stack.pop())
        return st

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends