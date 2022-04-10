#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution{
    public :
    string longestCommonPrefix(vector<string>& strs) {
        if (strs == NULL || strs.length == 0) return "";
        for (int i = 0; i < strs[0].length() ; i++){
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j ++) {
                if (i == strs[j].length() || strs[j].charAt(i) != c)
                    return strs[0].substring(0, i);             
            }
        }
        return strs[0];
    }
};

int main(int argc, char** argv){
    Solution solution;
    vector<string> s;
    for(int i=1;i<argc;i++){
        s.push_back(argv[i]);
    }
    result = solution.longestCommonPrefix(s[0]);
    cout << result << endl;
    return EXIT_SUCCESS;
}