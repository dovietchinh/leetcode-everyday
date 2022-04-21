// https://github.com/dovietchinh/letcode-everyday/blob/master/source/problem19.cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution{
	public:
		vector<int> buildArray(vector<int> &nums){
			vector<int> result;
			for(int i=0;i<nums.size();i++){
				result.push_back(nums[nums[i]]);
			}
			return result;
		}
};

int main(int argc, char** argv){
	Solution solution;
	vector<int> x = {0,2,1,5,3,4};
	vector<int> result = solution.buildArray(x);
	for(auto i:result){
		cout << i << " ";
	}
	cout << endl;
	return EXIT_SUCCESS;
}
