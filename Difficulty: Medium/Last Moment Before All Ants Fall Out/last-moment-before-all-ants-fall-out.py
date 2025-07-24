class Solution:
    def getLastMoment(self, n, left, right):
        # Max time for left-moving ants to fall off at position 0
        max_left = max(left) if left else 0
        # Max time for right-moving ants to fall off at position n
        max_right = max([n - r for r in right]) if right else 0
        # Return the maximum time any ant falls off
        return max(max_left, max_right)