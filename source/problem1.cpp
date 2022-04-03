#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    Solution() {
        int abc =10;
    }
    vector<int> twoSum(vector<int>& vec, int target) {
        vector<int> result;
        for (vector<int>::iterator ptr=vec.begin(); ptr!=vec.end(); ptr++){
            for (vector<int>::iterator ptr2=ptr+1; ptr2!=vec.end(); ptr2++){
                if((*ptr + *ptr2) == target){
                    result.push_back(ptr-vec.begin());
                    result.push_back(ptr2-vec.begin());
                }
            }
        }
        return result;
    }
};
int main(int argc, char** argv){
    Solution x;
    vector<int> vec = {2,7,11,15};
    int target = 9;
    vec = x.twoSum(vec,target);
    for(auto y : vec){
        cout << y << endl;
    }
    return EXIT_SUCCESS;
}
