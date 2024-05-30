//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    int mod=1e9+7;
    int countWays(string s1, string s2) {
        // code here
        int n=s1.size();
        int m=s2.size();

        vector<vector<int>> dp(n+1, vector<int> (m+1, 0));

        for (int i=0; i<=n; i++) 
            dp[i][0]=1;


        for(int i=1; i<=n; i++){
            for(int j=1; j<=m;j++){
                if(s1[i-1]==s2[j-1]){
                    dp[i][j]=(dp[i-1][j-1]%mod+dp[i-1][j]%mod)%mod;
                }
                else {
                    dp[i][j]=dp[i-1][j]%mod;
                }
            }
        }
        return dp[n][m]%mod;
    }
};



//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        string s1;
        getline(cin, s1);

        string s2;
        getline(cin, s2);

        Solution obj;
        int res = obj.countWays(s1, s2);

        cout << res << endl;
    }
}

// } Driver Code Ends