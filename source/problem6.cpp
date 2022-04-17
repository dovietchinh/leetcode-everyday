#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution{
    public :
    string longestCommonPrefix(vector<string>& strs) {
    //    if (strs == NULL || strs.size() == 0) return "";
        for (int i = 0; i < strs[0].length() ; i++){
            char c = strs[0][i];
            for (int j = 1; j < strs.size(); j ++) {
                if (i == strs[j].length() || strs[j][i] != c)
                    return strs[0].substr(0, i);             
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
    string result = solution.longestCommonPrefix(s);
    cout << result << endl;
    return EXIT_SUCCESS;
}
