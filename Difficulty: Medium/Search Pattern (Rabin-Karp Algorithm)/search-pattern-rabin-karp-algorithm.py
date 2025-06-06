class Solution:
    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        d = 256  # number of characters in input alphabet
        q = 101  # a prime number for hashing

        result = []
        p = 0  # hash value for pattern
        t = 0  # hash value for text
        h = 1

        # The value of h would be "pow(d, M-1) % q"
        for i in range(m - 1):
            h = (h * d) % q

        # Calculate the hash value of pattern and first window of text
        for i in range(m):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        # Slide the pattern over text one by one
        for i in range(n - m + 1):
            # Check the hash values of current window of text and pattern
            if p == t:
                # If the hash values match then only check for characters one by one
                if txt[i:i + m] == pat:
                    result.append(i + 1)  # 1-based indexing

            # Calculate hash value for next window of text:
            # Remove leading digit, add trailing digit
            if i < n - m:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
                # We might get negative value of t, converting it to positive
                if t < 0:
                    t += q

        return result