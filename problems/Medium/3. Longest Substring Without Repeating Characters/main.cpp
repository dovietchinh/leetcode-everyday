#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s){
        size_t size = s.size();
        for(int i=size;i>=1;i--){
            for(int j=0;j<size-i+1;j++){
                string substr = s.substr(j,i);
                if(this->unique(substr)){
                    return i;
                }
            }
        }
        return 0;
    }
    
    bool unique(string s){
        map<char,int> map2;
        for(auto key: s){
            if(map2.count(key)==0){
                map2[key] = 0;
            }
            map2[key] ++;
            if (map2[key]==2){
                return false;
            }
        }
        return true;
    }
    
};

int main(){
    vector<string> list({"au","rwwekq"});
    for (auto i: list){
        cout << Solution().lengthOfLongestSubstring(i) << endl;
    }
}