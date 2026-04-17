class Solution:
    def canFormPalindrome(self, s):
        freq = [0] * 26
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        odd_count = 0
        
        for count in freq:
            if count % 2 != 0:
                odd_count += 1
        
        return odd_count <= 1