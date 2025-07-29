class Solution:
    def asciirange(self, s):
        result = []
        positions = {}

        # Record the first and last occurrence of each character
        for i, ch in enumerate(s):
            if ch not in positions:
                positions[ch] = [i, i]
            else:
                positions[ch][1] = i

        # For each character, if it appears more than once, compute sum between
        for ch in positions:
            start, end = positions[ch]
            if start != end:  # Character appears more than once
                ascii_sum = sum(ord(s[i]) for i in range(start + 1, end))
                if ascii_sum > 0:
                    result.append(ascii_sum)

        return result