//{ Driver Code Starts
//Initial template for JAVA

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG
 {
	public static void main (String[] args) throws IOException
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int t = Integer.parseInt(br.readLine());
	    for(int i=0;i<t;i++){
	        int n = Integer.parseInt(br.readLine());
	        String l = br.readLine();
    		String[] sarr = l.split(" ");
    		int[] arr = new int[sarr.length];
    		for(int i1=0;i1<arr.length;i1++){
    			arr[i1] = Integer.parseInt(sarr[i1]);
    		}
    		
            Solution obj = new Solution();
            
            int[] res = obj.twoRepeated(arr, n);
            System.out.println(res[0] + " " + res[1]);
	    }
	}
}
// } Driver Code Ends


//User function template for JAVA

class Solution
{
    //Function to find two repeated elements.
    public int[] twoRepeated(int arr[], int n)
    {
        // Your code here
        //s1
         int ans[] = new int[2];
        int k=0;
        int flag = 0;

        //s2 traverse in arr
        for(int i=0; i<n+2;i++){
            if(arr[Math.abs(arr[i])] >0){
                arr[Math.abs(arr[i])] = - arr[Math.abs(arr[i])];

            }
            else{
                if(flag==0){
                    ans[k++] = Math.abs(arr[i]);
                    flag=1;
                }
                else{
                    ans[k++]  =  Math.abs(arr[i]);
                }
            }
        }
         return ans;


    }
}