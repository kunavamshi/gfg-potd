//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String s = read.readLine();

            Solution ob = new Solution();
            String result = ob.removeDups(s);

            System.out.println(result);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    String removeDups(String str) {
        // To keep track of already seen characters
        boolean[] seen = new boolean[26];
        // To store the result string
        StringBuilder sb = new StringBuilder();

        // Iterate through the given string
        for (char ch : str.toCharArray()) {
            // Calculate the index for the current character
            int index = ch - 'a';
            // If the character has not been seen before, add it to the result
            if (!seen[index]) {
                sb.append(ch);
                seen[index] = true; // Mark the character as seen
            }
        }

        return sb.toString();
    }
}