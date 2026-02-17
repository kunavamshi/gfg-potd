class Solution:
    def overlapInt(self, arr):
        events = []
        
        for start, end in arr:
            events.append((start, 1))       # interval starts
            events.append((end + 1, -1))    # interval ends (inclusive handling)
        
        events.sort()
        
        max_overlap = 0
        current = 0
        
        for _, delta in events:
            current += delta
            max_overlap = max(max_overlap, current)
        
        return max_overlap