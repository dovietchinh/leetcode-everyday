//https://leetcode.com/problems/max-increase-to-keep-city-skyline/
#include <vector>
#include <string>
#include <climits>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution{
	public:
		int maxIncreaseKeepSkyline(const vector<vector<int>>& grid){
			vector<int> max_rows,max_columns;
			int height = grid.size();
			int width = grid[0].size();
			for(int j =0; j < width;j++)
				max_columns.push_back(INT_MIN);
			for(int j =0; j < width; j++)
				max_rows.push_back(INT_MIN);
			for(int i=0;i<height;i++){
				for(int j=0;j<width;j++){
					if(grid[i][j] > max_rows[i]) max_rows[i] = grid[i][j];
					if(grid[i][j] > max_columns[j]) max_columns[j] = grid[i][j];
				}
			};
			int result = 0;
			for(int i=0;i<height;i++){
				for(int j=0;j<width;j++){
					result += -grid[i][j] + std::min(max_rows[i],max_columns[j]);
				}
			}
			return result;
		}
};


int main(int argc, char** argv){
	Solution solution;
	vector<vector<int>> grid = {
		{3,0,8,4},
		{2,4,5,7},
		{9,2,6,3},
		{0,3,1,0},
	};
	int result = solution.maxIncreaseKeepSkyline(grid);
	cout << result << endl;
	return EXIT_SUCCESS;
}
