class Solution:
    def nodeSum(self, root, l, r):
        # Base case
        if not root:
            return 0
        
        # If node's value is less than l, ignore left subtree
        if root.data < l:
            return self.nodeSum(root.right, l, r)
        
        # If node's value is greater than r, ignore right subtree
        if root.data > r:
            return self.nodeSum(root.left, l, r)
        
        # Otherwise, include this node and explore both subtrees
        return root.data + self.nodeSum(root.left, l, r) + self.nodeSum(root.right, l, r)