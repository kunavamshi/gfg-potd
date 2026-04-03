class Solution {
  public:
    vector<int> diagView(vector<vector<int>> mat) {
        int n = mat.size();
        vector<int> result;

        // Traverse all possible sums of indices
        for (int s = 0; s <= 2*n - 2; s++) {
            for (int i = 0; i < n; i++) {
                int j = s - i;
                if (j >= 0 && j < n) {
                    result.push_back(mat[i][j]);
                }
            }
        }

        return result;
    }
};