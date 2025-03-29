//{ Driver Code Starts
// Driver code
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
   public:
     vector<int> jobSequencing(vector<int> &deadline, vector<int> &profit) {
         // code here
         int n=deadline.size();
         vector<pair<int,int>>v;
         for(int i=0;i<n;i++){
             v.push_back({deadline[i], profit[i]});
         }
         sort(v.begin(), v.end());
         
         priority_queue<int, vector<int>, greater<int>>pq;
         int curr=0, points=0;
         for(int i=0;i<n;i++){
             if(v[i].first > curr){
                 curr++;
                 points+=v[i].second;
                 pq.push(v[i].second);
             }
             else if(v[i].second > pq.top()){
                 points-=pq.top();
                 pq.pop();
                 points+=v[i].second;
                 pq.push(v[i].second);
             }
         }
         return {curr, points};
         
     }
 };


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> deadlines, profits;
        string temp;
        getline(cin, temp);
        int x;
        istringstream ss1(temp);
        while (ss1 >> x)
            deadlines.push_back(x);

        getline(cin, temp);
        istringstream ss2(temp);
        while (ss2 >> x)
            profits.push_back(x);

        Solution obj;
        vector<int> ans = obj.jobSequencing(deadlines, profits);
        cout << ans[0] << " " << ans[1] << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends