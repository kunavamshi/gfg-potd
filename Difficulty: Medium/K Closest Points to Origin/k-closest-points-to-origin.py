import heapq

class Solution:
    def kClosest(self, points, k):
        # Max heap to keep track of k closest points
        heap = []
        
        for x, y in points:
            dist = -(x * x + y * y)  # Negative for max-heap behavior
            heapq.heappush(heap, (dist, x, y))
            
            # Keep heap size limited to k
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract k closest points
        return [[x, y] for (_, x, y) in heap]