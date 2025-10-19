class Solution:
    def getKClosest(self, root, target, k):
        # Helper: inorder traversal (gives sorted order)
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)
        
        values = inorder(root)
        
        # Sort based on absolute difference, then by value
        values.sort(key=lambda x: (abs(x - target), x))
        
        # Return first k closest values
        return values[:k]