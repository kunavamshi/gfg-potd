class Solution:
    def isSumString(self, s: str) -> bool:
        # Helper to check if string has valid number format
        def isValid(num):
            return not (len(num) > 1 and num[0] == '0')

        # Recursive function to check if remaining string matches the sum condition
        def check(s, num1, num2):
            if not isValid(num1) or not isValid(num2):
                return False

            sum_str = str(int(num1) + int(num2))
            if not s.startswith(sum_str):
                return False
            if len(s) == len(sum_str):
                return True
            return check(s[len(sum_str):], num2, sum_str)

        n = len(s)
        # Try all combinations for first and second numbers
        for i in range(1, n):
            for j in range(1, n - i):
                num1 = s[0:i]
                num2 = s[i:i + j]
                if check(s[i + j:], num1, num2):
                    return True
        return False