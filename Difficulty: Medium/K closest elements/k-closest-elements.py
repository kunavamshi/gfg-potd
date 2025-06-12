class Solution:
    def printKClosest(self, arr, k, x):
        filtered = [num for num in arr if num != x]
        # Sort by closeness to x, tie-breaker: prefer larger element
        filtered.sort(key=lambda num: (abs(num - x), -num))
        return filtered[:k]