class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Dictionary to store the horizontal distance and the corresponding node's data
        hd_node_map = {}
        # Queue for level order traversal
        queue = deque([(root, 0)])  # Each element is a tuple (node, horizontal distance)

        while queue:
            node, hd = queue.popleft()
            
            # Update the dictionary with the current node for this horizontal distance
            hd_node_map[hd] = node.data
            
            # If there is a left child, add it to the queue with hd - 1
            if node.left:
                queue.append((node.left, hd - 1))
            
            # If there is a right child, add it to the queue with hd + 1
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Extract the bottom view from the dictionary and sort by horizontal distance
        bottom_view = [hd_node_map[hd] for hd in sorted(hd_node_map)]
        return bottom_view

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
from collections import deque
from collections import defaultdict
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.bottomView(root)
        for i in res:
            print (i, end = " ")
        print()


# } Driver Code Ends