class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def constructTree(self, pre, post):
        self.preIndex = 0
        postIndexMap = {val: idx for idx, val in enumerate(post)}
        
        def construct(l, r):
            if self.preIndex >= len(pre) or l > r:
                return None
            
            root = Node(pre[self.preIndex])
            self.preIndex += 1
            
            # if there are still nodes to be constructed
            if l == r or self.preIndex >= len(pre):
                return root
            
            # find the next node in postorder
            nextVal = pre[self.preIndex]
            mid = postIndexMap[nextVal]
            
            # recursively build left and right subtrees
            root.left = construct(l, mid)
            root.right = construct(mid + 1, r - 1)
            
            return root
        
        return construct(0, len(post) - 1)