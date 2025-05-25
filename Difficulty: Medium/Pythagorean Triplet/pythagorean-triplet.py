class Solution:
    def pythagoreanTriplet(self, arr):
        # Square every element
        squared = [x * x for x in arr]
        squared_set = set(squared)
        n = len(squared)

        # Check every pair (i, j) to see if their sum exists as c^2
        for i in range(n):
            for j in range(i + 1, n):
                if squared[i] + squared[j] in squared_set:
                    return True
        return False