from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Convert all numbers to strings for comparison
        arr = list(map(str, arr))

        # Custom comparator
        def compare(x, y):
            # If x+y is greater than y+x, x should come before y
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))

        # Concatenate result
        result = "".join(arr)

        # Edge case: when result has leading zeros (e.g., [0, 0])
        return "0" if result[0] == "0" else result