// https://leetcode.com/problems/subrectangle-queries/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class SubrectangleQueries{
	public:
		vector<vector<int>> rectangle;
		SubrectangleQueries(vector<vector<int>>& rectangle) {
			this->rectangle = rectangle;
	    }
    
	    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        	for(int r=row1;r<row2;r++)
				for(int c=col1;c<col2;c++)
					this->rectangle[r][c] = newValue;
    	}
    
    	int getValue(int row, int col) {
			return this->rectangle[row][col];
	    }	
};

int main(int argc, char** argv){
	vector<vector<int>> rectangle = {
		{1,2,1},
		{4,3,4},
		{3,2,1},
		{1,1,1},
	}	
	auto p = SubrectangleQueries(rectangle);
	p.updateSubrectangle(0,0,3,2,5);
	for (auto i: p.rectangle)
		for(auto j:i)
			cout << j << " ";
	cout << endl;
	return 1;
}
