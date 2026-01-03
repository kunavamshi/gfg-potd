class Solution:
    def flatten(self, root):
        if not root or not root.next:
            return root
        
        # Flatten the rest of the list
        root.next = self.flatten(root.next)
        
        # Merge current list with flattened next list
        return self.merge(root, root.next)
    
    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        
        if a.data <= b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
        
        result.next = None  # critical: remove next pointers
        return result