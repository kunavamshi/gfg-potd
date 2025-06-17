import java.util.*;

class Solution {
    public int minimumCoins(int[] arr, int k) {
        Arrays.sort(arr);
        int n = arr.length;

        long[] prefixSum = new long[n + 1];
        long[] suffixSum = new long[n + 1];

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + arr[i];
        }

        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + arr[i];
        }

        long minCoins = Long.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int base = arr[i];
            int maxAllowed = base + k;

            // Binary search: find first index where arr[j] > maxAllowed
            int idx = upperBound(arr, maxAllowed);

            long removeBefore = prefixSum[i];

            // All elements from idx to n-1 must be reduced to maxAllowed
            long reduceAfter = suffixSum[idx] - (long)(n - idx) * maxAllowed;

            long total = removeBefore + reduceAfter;
            minCoins = Math.min(minCoins, total);
        }

        return (int)minCoins;
    }

    private int upperBound(int[] arr, int target) {
        int low = 0, high = arr.length;
        while (low < high) {
            int mid = (low + high) / 2;
            if (arr[mid] <= target) low = mid + 1;
            else high = mid;
        }
        return low;
    }
}