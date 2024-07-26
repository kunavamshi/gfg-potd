//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            String str = sc.nextLine();
            int k = Integer.parseInt(sc.nextLine().trim());
            Solution obj = new Solution();
            if (obj.kPangram(str, k))
                System.out.println("true");
            else
                System.out.println("false");
        }
    }
}
// } Driver Code Ends


// User function Template for Java
class Solution {
    boolean kPangram(String str, int k) {
        // code here
        int ch_cnt=0;
        int freq[] = new int[26];
        for( char ch : str.toCharArray()){
            if(ch==' ')
            continue;
            else{
                freq[ch-'a']++;
                ch_cnt++;
            }
        }
         int cnt=0; // ch not present
        for(int i=0; i<26; i++){
            if(freq[i]==0)
            cnt++;
        }
        return( ch_cnt>=26 && cnt<=k );
    }
}