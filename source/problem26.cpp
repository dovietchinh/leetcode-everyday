// https://leetcode.com/problems/number-of-good-pairs/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution{
	public:
		int numIdenticalPairs(vector<int> &nums){
			vector<int> unique = this->getUnique(nums);
			int result = 0;
			for(auto x: unique){
				int cout = std::count(nums.begin(),nums.end(),x);
				result += cout*(cout-1)/2;
			}
			return result;
		};
		vector<int> getUnique(vector<int> nums){
			std::sort(nums.begin(),nums.end());
			vector<int>::iterator i = std::unique(nums.begin(),nums.end());
			nums.resize(std::distance(nums.begin(),i));
			return nums;
		};
};

int main(int argc, char** argv){
	Solution solution;
	vector<int> nums = {1,2,3};
	cout << solution.numIdenticalPairs(nums) << endl;
	return EXIT_SUCCESS;
}
