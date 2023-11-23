#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
    public:
        int balancedStringSplit(string s) {
            int r=0,c=0;
            for(int i=0;i<s.length();i++){
                if(s[i]=='R') c++;
                else c--;
                if(c==0) r++;
            }
            return r;
        }
};

int main(int argc, char** argv){
    // Solution a;
    vector<string> input{"RLRRLLRLRL","RLRRRLLRLL","LLLLRRRR"};
    for(string i : input){
        int r = Solution().balancedStringSplit(i);
        cout << "r: " << r << endl;
    };
    return 1;  
};