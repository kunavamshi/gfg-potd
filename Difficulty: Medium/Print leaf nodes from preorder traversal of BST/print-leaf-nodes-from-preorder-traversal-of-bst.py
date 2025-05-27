class Solution:
    def leafNodes(self, preorder):
        self.i = 0
        n = len(preorder)
        result = []

        def findLeaves(min_val, max_val):
            if self.i >= n or preorder[self.i] < min_val or preorder[self.i] > max_val:
                return False
            
            root_val = preorder[self.i]
            self.i += 1

            # Simulate left subtree
            is_left = findLeaves(min_val, root_val - 1)
            # Simulate right subtree
            is_right = findLeaves(root_val + 1, max_val)

            # If no children, it's a leaf
            if not is_left and not is_right:
                result.append(root_val)
            return True

        findLeaves(float('-inf'), float('inf'))
        return result