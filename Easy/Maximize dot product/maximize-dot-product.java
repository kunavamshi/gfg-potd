//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    int n = sc.nextInt();
                    int m = sc.nextInt();
                    int a[] = new int[n];
                    int b[] = new int[m];
                    for(int i = 0;i<n;i++)
                        a[i] = sc.nextInt();
                    for(int i = 0;i<m;i++)
                        b[i] = sc.nextInt();    
                    Solution ob = new Solution();
                    System.out.println(ob.maxDotProduct(n, m, a, b));
                }
        }
}    
// } Driver Code Ends


//User function Template for Java

//  User function Template for Java

class Solution{
    
	public int maxDotProduct(int n, int m, int a[], int b[]) { 
		// Your code goes here
	
		 // Initializing a 2D array to store the maximum dot product
                 int[][] gp = new int[m + 1][n + 1];
        
                 // Initializing the array with zeros
                 for (int[] row : gp) {
                     Arrays.fill(row, 0);
                 }
        
                 // Dynamic programming approach to calculate the maximum dot product
                 for (int i = 1; i <= m; i++) {
                     for (int j = i; j <= n; j++) {
                     // Calculating the current dot product and update the cell
                     gp[i][j] = Math.max(gp[i - 1][j - 1] + a[j - 1] * b[i - 1], gp[i][j - 1]);
                     }
                 }
        
                // Returning the maximum dot product
                return gp[m][n];
	} 
}