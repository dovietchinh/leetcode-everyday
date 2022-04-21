// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

#include <iostream>
#include <vector>

using namespace std;

class Solution{
	public:
		bool canBeIncreasing(vector<int> &nums){
			size_t n = nums.size();
			int previous = nums[0];
			int count = 0;
			if(n==3){
				if(nums[0]<nums[2] | nums[1] < nums[2] | nums[0] <nums[1]){
						return true;
				}
				else{
						return false;
				}
			}
			for(int i=1;i<n-1;i++){
				if(previous<nums[i+1]){
					if(nums[i]<previous | nums[i] > nums[i+1]){
						count ++;
						continue;
					}
					else{
						previous = nums[i];
					}
				}
				else {		
				return false;
				}
			}
			return count <=1;
		}
};

int main(int argc, char** argv){
//	vector<int> x = {1,2,10,5,7,2,9};
	vector<int> x = {105,924,32,968};
	Solution solution;
	bool result =  solution.canBeIncreasing(x);
	cout << "result:: "<< result<< endl;
	return EXIT_SUCCESS;
}
