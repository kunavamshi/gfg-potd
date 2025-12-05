class Solution:
    def minCost(self, costs):
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])

        # If only one color exists but multiple walls → impossible
        if k == 1:
            return costs[0][0] if n == 1 else -1

        min1 = 0
        min2 = 0
        idx1 = -1

        for i in range(n):
            new_min1 = float('inf')
            new_min2 = float('inf')
            new_idx1 = -1

            for c in range(k):
                # use min2 if same color as previous best
                cost = costs[i][c] + (min2 if c == idx1 else min1)

                if cost < new_min1:
                    new_min2 = new_min1
                    new_min1 = cost
                    new_idx1 = c
                elif cost < new_min2:
                    new_min2 = cost

            min1, min2, idx1 = new_min1, new_min2, new_idx1

        return min1