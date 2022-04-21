// https://leetcode.com/problems/relative-sort-array/submissions/
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <utility>

using namespace std;

map<int,int> mymap;
int size_;
class Solution{
	public:
		vector<int> relativeSortArray(vector<int> arr1, vector<int> arr2){
			mymap.clear();
			size_ = arr2.size();			
			for(int i=0;i<arr2.size();i++){
				mymap.insert(pair<int,int>(arr2[i],i));
			};
			sort(arr1.begin(),arr1.end(),myfunction);
			return arr1;
		};

		static bool myfunction(int x,int y){
			int value_x = size_;
			int value_y = size_;
			if(mymap.count(x)==1){
				value_x = mymap[x];
			}
			if(mymap.count(y)==1){
				value_y = mymap[y];
			}
			if(mymap.count(x)==0 && mymap.count(y)==0)
			{
					return x<y;
			}

			return value_x <=value_y;
		};


};


int main(int argc, char** argv){
	vector<int> arr1 = {2,3,1,3,2,4,6,7,9,2,19};
	vector<int> arr2 = {2,1,4,3,9,6};
	Solution solution;
	vector<int> result = solution.relativeSortArray(arr1,arr2);
	for(auto x: result){
		cout << x << " ";
	}
	cout << endl;
	return EXIT_SUCCESS;
}
