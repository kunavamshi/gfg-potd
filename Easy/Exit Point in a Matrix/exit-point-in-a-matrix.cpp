//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
public:
    vector<int> FindExitPoint(int n, int m, vector<vector<int>>& matrix) {
        // Define directions: right, down, left, up (clockwise)
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int dir = 0; // start with moving right
        int x = 0, y = 0; // starting position
        while (x >= 0 && x < n && y >= 0 && y < m) {
            if (matrix[x][y] == 1) {
                // Change direction to the right
                dir = (dir + 1) % 4;
                // Mark the cell as visited
                matrix[x][y] = 0;
            } else {
                // Move in the current direction
                x += directions[dir].first;
                y += directions[dir].second;
            }
        }
        // Exit point is the last visited cell
        return {x - directions[dir].first, y - directions[dir].second};
    }
};


//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> matrix(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> matrix[i][j];
        Solution obj;
        vector<int> ans = obj.FindExitPoint(n, m, matrix);
        for (auto i : ans)
            cout << i << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends