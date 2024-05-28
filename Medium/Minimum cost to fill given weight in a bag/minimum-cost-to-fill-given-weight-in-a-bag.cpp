//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &A, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A) {
        for (int i = 0; i < A.size(); i++) {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {

    long long int dp[201][201]; // Define the dp array

    long long int helper(std::vector<int>& cost, int n, int w) {
        if (w == 0) return 0;  // Base case: no cost for weight 0
        if (n == 0 || w < 0) return INT_MAX;  // Base case: no solution

        if (dp[n][w] != -1) return dp[n][w];  // Check if already computed

        if (n <= w && cost[n-1] != -1) {
            return dp[n][w] = std::min(cost[n-1] + helper(cost, n, w - n), helper(cost, n - 1, w));
        }
        return dp[n][w] = helper(cost, n - 1, w);  // Exclude the current item
    }

public:
    int minimumCost(int n, int w, std::vector<int> &cost) {
        memset(dp, -1, sizeof(dp));  // Initialize dp array with -1
        long long int res = helper(cost, n, w);  // Call the helper function
        return res >= INT_MAX ? -1 : static_cast<int>(res);  // Handle the result
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        int w;
        scanf("%d", &w);

        vector<int> cost(n);
        Array::input(cost, n);

        Solution obj;
        int res = obj.minimumCost(n, w, cost);

        cout << res << endl;
    }
}

// } Driver Code Ends