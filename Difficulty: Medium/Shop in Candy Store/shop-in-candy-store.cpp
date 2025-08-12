class Solution {
  public:
    vector<int> minMaxCandy(vector<int>& prices, int k) {
        sort(prices.begin(), prices.end());
        int n = prices.size();
        
        // Minimum Cost Calculation
        int minCost = 0;
        int i = 0, j = n - 1;
        while (i <= j) {
            minCost += prices[i];  // Buy the cheapest one
            i++;
            j -= k;  // Get k most expensive ones for free
        }

        // Maximum Cost Calculation
        int maxCost = 0;
        i = 0, j = n - 1;
        while (i <= j) {
            maxCost += prices[j];  // Buy the most expensive one
            j--;
            i += k;  // Get k cheapest ones for free
        }

        return {minCost, maxCost};
    }
};