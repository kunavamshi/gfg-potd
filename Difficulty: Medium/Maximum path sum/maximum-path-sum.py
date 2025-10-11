class Solution:
    def findMaxSum(self, root):
        # Initialize global max sum as the smallest integer
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # Compute max path sum from left & right subtrees; ignore negatives
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Max path sum passing through this node
            current_sum = node.data + left + right

            # Update global max if needed
            self.max_sum = max(self.max_sum, current_sum)

            # Return max gain if we continue from this node upwards
            return node.data + max(left, right)
        
        dfs(root)
        return self.max_sum