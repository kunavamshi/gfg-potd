class Solution:
    def minCost(self, n, m, x, y):
        # Sort cuts in descending order (greedy choice)
        x.sort(reverse=True)
        y.sort(reverse=True)
        
        i = j = 0  # pointers for x and y cuts
        hz_segments = 1
        vt_segments = 1
        cost = 0
        
        # Process until one array is finished
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                # vertical cut
                cost += x[i] * hz_segments
                vt_segments += 1
                i += 1
            else:
                # horizontal cut
                cost += y[j] * vt_segments
                hz_segments += 1
                j += 1
        
        # Remaining vertical cuts
        while i < len(x):
            cost += x[i] * hz_segments
            vt_segments += 1
            i += 1
        
        # Remaining horizontal cuts
        while j < len(y):
            cost += y[j] * vt_segments
            hz_segments += 1
            j += 1
        
        return cost