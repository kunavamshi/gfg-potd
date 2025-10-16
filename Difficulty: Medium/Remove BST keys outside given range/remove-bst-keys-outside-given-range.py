class Solution:
    def removekeys(self, root, l, r):
        # Base case
        if not root:
            return None

        # Recur for left and right subtrees
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)

        # If current node is smaller than l, discard left subtree
        if root.data < l:
            return root.right

        # If current node is greater than r, discard right subtree
        if root.data > r:
            return root.left

        # If current node is within range, keep it
        return root