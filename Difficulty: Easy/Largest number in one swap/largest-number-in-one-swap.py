class Solution:
    def largestSwap(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        # Step 1: Precompute the rightmost position of each digit
        last_index = {str(d): -1 for d in range(10)}
        for i in range(n):
            last_index[s[i]] = i   # store rightmost index of digit
        
        # Step 2: Traverse left to right, try to swap with a bigger digit
        for i in range(n):
            # Try digits from '9' down to one greater than current
            for d in range(9, int(s[i]), -1):
                if last_index[str(d)] > i:  # bigger digit exists to the right
                    # Perform swap
                    j = last_index[str(d)]
                    s[i], s[j] = s[j], s[i]
                    return "".join(s)
        
        # If no beneficial swap, return original
        return "".join(s)