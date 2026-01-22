class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        # ---------- SUM OF SUBARRAY MAXIMUMS ----------
        prev_greater = [-1] * n
        next_greater_eq = [n] * n

        st = []
        # prev greater (strict >)
        for i in range(n):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            prev_greater[i] = st[-1] if st else -1
            st.append(i)

        st = []
        # next greater or equal (>=)
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            next_greater_eq[i] = st[-1] if st else n
            st.append(i)

        max_sum = 0
        for i in range(n):
            left = i - prev_greater[i]
            right = next_greater_eq[i] - i
            max_sum += arr[i] * left * right

        # ---------- SUM OF SUBARRAY MINIMUMS ----------
        prev_smaller = [-1] * n
        next_smaller_eq = [n] * n

        st = []
        # prev smaller (strict <)
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            prev_smaller[i] = st[-1] if st else -1
            st.append(i)

        st = []
        # next smaller or equal (<=)
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            next_smaller_eq[i] = st[-1] if st else n
            st.append(i)

        min_sum = 0
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller_eq[i] - i
            min_sum += arr[i] * left * right

        return max_sum - min_sum