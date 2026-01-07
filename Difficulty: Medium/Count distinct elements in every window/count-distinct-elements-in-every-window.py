class Solution:
    def countDistinct(self, arr, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        result = []
        distinct = 0
        
        # Initialize first window
        for i in range(k):
            if freq[arr[i]] == 0:
                distinct += 1
            freq[arr[i]] += 1
        
        result.append(distinct)
        
        # Slide the window
        for i in range(k, len(arr)):
            # Remove outgoing element
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                distinct -= 1
            
            # Add incoming element
            incoming = arr[i]
            if freq[incoming] == 0:
                distinct += 1
            freq[incoming] += 1
            
            result.append(distinct)
        
        return result