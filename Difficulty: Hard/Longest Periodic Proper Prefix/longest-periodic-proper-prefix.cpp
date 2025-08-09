class Solution {
  public:
    int getLongestPrefix(string &s) {
        // code here
         int n = s.size();
        int len = s.size()-1;
        
        while(len){
            int sPtr = len;
            int i = 0;
            
            while(sPtr<n){
                if(s[sPtr] == s[i]){
                    i++;
                    sPtr++;
                }
                else{
                    break;
                }
            }
            
            if(sPtr==n)
              return len;
            
            len--;
        }
        
        
        return -1;
    }
};