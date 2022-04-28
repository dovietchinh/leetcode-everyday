// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

class Solution{
	public:
		vector<int> minOperations(string boxes){
			vector<int> result;
			size_t n = boxes.length();
			for(int i=0;i<n;i++){
				int temp = 0;
				for(int j=0;j<n;j++){
					if(boxes[j] == '1') temp += abs(i-j);
				}
				result.push_back(temp);
			}
			return result;
			
		};
};

int main(int argc, char** argv){
	string boxes = "001011";
	Solution solution;
	vector<int> result = solution.minOperations(boxes);
	for(auto i:result){
		cout << i << " ";
	}
	cout << endl;
	return EXIT_SUCCESS;
}
