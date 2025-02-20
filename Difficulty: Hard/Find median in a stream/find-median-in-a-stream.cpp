//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    vector<double> getMedian(vector<int> &arr) {
        //CodeGenius
        priority_queue<int>leftmaxheap;
        priority_queue<int,vector<int>,greater<int>>rightminheap;
        vector<double>ans;
        for(int i=0;i<arr.size();i++){
            leftmaxheap.push(arr[i]);
            
            int ele=leftmaxheap.top();
            rightminheap.push(ele);
            leftmaxheap.pop();
            
            if(rightminheap.size()>leftmaxheap.size()){
                int ele=rightminheap.top();
                leftmaxheap.push(ele);
                rightminheap.pop();
            }
            double median;
            if(leftmaxheap.size()!=rightminheap.size())
            median=leftmaxheap.top();
            else
            median=(double)(leftmaxheap.top()+rightminheap.top())/2;
            ans.push_back(median);
        }
        return ans;
    }
};



//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        string s;
        getline(cin, s);
        stringstream ss(s);
        vector<int> nums;
        int num;
        while (ss >> num) {
            nums.push_back(num);
        }
        Solution ob;
        vector<double> ans = ob.getMedian(nums);
        cout << fixed << setprecision(1);
        for (auto &i : ans)
            cout << i << " ";
        cout << "\n";
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends