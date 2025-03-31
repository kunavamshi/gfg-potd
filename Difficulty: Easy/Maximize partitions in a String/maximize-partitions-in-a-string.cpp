//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
   public:
     int maxPartitions(string &s) {
         vector<int> v(26,0);
         for(char c:s){
             v[c-'a']++;
         }
         unordered_map<int,int>mp;
         int ans = 0;
         for(int i = 0 ; i<s.size(); i++){
             char c = s[i];
             mp[c-'a']++;
             bool e = true;
             for(auto d:mp){
                 if(v[d.first] != d.second){
                     e = false;
                 }
             }
             if(e == true){
                ans++;
                mp = {};
             }
         }
         return ans;
         
     }
 };

//{ Driver Code Starts.

int main() {
    int tc;
    cin >> tc;

    for (int i = 0; i < tc; ++i) {
        string s;
        cin >> s;
        Solution obj;
        cout << obj.maxPartitions(s) << endl;
        cout << "~" << endl;
    }

    return 0;
}

// } Driver Code Ends