class Solution:
    def countValid(self, n, arr):
        bad_digits = set(arr)
        all_digits = set(range(10))
        good_digits = list(all_digits - bad_digits)

        if not good_digits:
            return 0  # No valid digit left to form a number

        # Count of total n-digit numbers
        total = 9 * (10 ** (n - 1)) if n > 1 else 9

        # Count n-digit numbers formed only using good_digits
        def count_only_good_digits():
            count = 0
            for first in good_digits:
                if n == 1:
                    if first != 0:
                        count += 1
                elif first != 0:
                    # First digit can't be 0
                    count += len(good_digits) ** (n - 1)
            return count

        only_good = count_only_good_digits()

        return total - only_good