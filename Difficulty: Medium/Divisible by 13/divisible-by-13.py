class Solution:
    def divby13(self, s):
        remainder = 0
        for digit in s:
            remainder = (remainder * 10 + int(digit)) % 13
        return remainder == 0