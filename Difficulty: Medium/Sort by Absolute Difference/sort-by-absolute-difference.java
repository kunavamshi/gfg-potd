import java.util.*;

class Solution {
    public void rearrange(int[] arr, int x) {
        // Convert int[] to Integer[] for Comparator
        Integer[] temp = Arrays.stream(arr).boxed().toArray(Integer[]::new);

        // Stable sort with custom comparator
        Arrays.sort(temp, (a, b) -> {
            int diffA = Math.abs(a - x);
            int diffB = Math.abs(b - x);
            return diffA - diffB; // stable sort keeps original order if equal
        });

        // Copy back to arr
        for (int i = 0; i < arr.length; i++) {
            arr[i] = temp[i];
        }
    }
}