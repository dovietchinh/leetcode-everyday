#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution{
	public:
		vector<int> shuffle(vector<int> nums, int n){
	//		size_t n = nums.size();
			vector<int> result;
			for(int i=0;i<n;i++){
				result.push_back(nums.at(i));
				result.push_back(nums.at(i+n));
			}
			return result;
		}
};

int main(int argc, char** argv){
	Solution solution;
	vector<int> x = {2,5,1,3,4,7};
	vector<int> result = solution.shuffle(x,x.size()/2);
	for(auto i : result){
		cout << i << endl;
	}
	return EXIT_SUCCESS;
}

