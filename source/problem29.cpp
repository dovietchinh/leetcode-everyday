// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
		vector<pair<int,int>> temp;
		for(int i=0;i<nums.size();i++) temp.push_back(make_pair(nums[i],i));
		std::sort(temp.begin(),temp.end(),
				[](pair<int,int> x1, pair<int,int> x2){return x1.first < x2.first;});
		vector<int> result;
		result.resize(temp.size());
		for(int i=0;i<temp.size();i++){
			int value = temp[i].first;
			int index = temp[i].second;
			cout << "value:" << value << endl;
			int temp2 = i-std::count_if(temp.begin(),temp.begin()+i,[&value](const auto x){return x.first==value;});
			cout << "index :" << index << endl;
			result[index] = temp2;
		};
		return result;
    };
};

int main(int argc, char** argv){
	Solution solution;
	vector<int> nums = {8,1,2,2,3};
	vector<int> result = solution.smallerNumbersThanCurrent(nums);
	for(auto x: result) cout << x << " ";
	cout << endl;
	return EXIT_SUCCESS;
}
