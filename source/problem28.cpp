// https://leetcode.com/problems/jewels-and-stones/
#include <iostream>
#include <string>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
		int result = 0;
		for(auto i:jewels){
			result += std::count(stones.begin(),stones.end(),i);
		}    
		return result;
    };
};
int main(int argc, char** argv){
	Solution solution;
	string jewels = "aA";
	string stones = "aAAbbb";
	cout << solution.numJewelsInStones(jewels, stones) << endl;
	return EXIT_SUCCESS;
}
