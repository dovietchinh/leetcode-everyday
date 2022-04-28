// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
		vector<int> result;
		for(auto circle : queries){
			int temp = 0;
			for(auto point:points){
				float distance = pow((circle[0] - point[0]),2.0);
				distance += pow((circle[1] - point[1]),2.0);
				distance -= pow(circle[2],2.0);
				if(distance <= 0) temp++;	
			}
			result.push_back(temp);
		};
		return result;
    };
};

int main(){
	vector<vector<int>> points = {
	{1,3},{3,3},{5,3},{2,2}
	};
	vector<vector<int>> queries = {{2,3,1},{4,3,1},{1,1,2}};
	Solution solution;
	vector<int> result = solution.countPoints(points, queries);
	for(auto i: result) cout << i << " ";
	cout << endl;
	return EXIT_SUCCESS;
}
