#include <iostream> 
#include <vector>
using namespace std;
class Solution{
    public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
};

int main(int argc, char ** argv){
    Solution solution;
    vector<int> nums = {0,1,2,2,3,0,4,2};
    int val = 2;
    int result = solution.removeElement(nums,val);
    cout << result << endl;
    return EXIT_SUCCESS;
}