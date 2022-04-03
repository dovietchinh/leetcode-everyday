#include <vector>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv){
    ifstream f("../stdin.txt");
    int N;
    f >> N;
    // cout << N;
    vector<int> vec;
    for(int i =0;i<N;i++){
        int temp;
        f>> temp;
        vec.push_back(temp);
    }
    int a,b,c;
    f >> a >> b >> c;
    vec.erase(vec.begin()+a -1);
    vec.erase(vec.begin()+b -1,vec.begin()+c-1);
    cout << vec.size() << endl;
    for(auto x: vec){cout << x<< " ";}
    return EXIT_SUCCESS;
}