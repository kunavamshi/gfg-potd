from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
        
        # Dictionary to store nodes for each horizontal distance
        hd_map = defaultdict(list)
        
        # Queue for level order traversal
        queue = deque()
        queue.append((root, 0))   # (node, horizontal_distance)
        
        min_hd = max_hd = 0
        
        while queue:
            node, hd = queue.popleft()
            
            # Store node value in corresponding vertical line
            hd_map[hd].append(node.data)
            
            # Update range of horizontal distances
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            # Push left and right children
            if node.left:
                queue.append((node.left, hd - 1))
            
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Collect result from leftmost to rightmost
        result = []
        for hd in range(min_hd, max_hd + 1):
            result.append(hd_map[hd])
        
        return result