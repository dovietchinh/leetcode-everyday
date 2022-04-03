#include <string>
#include <map>
// #include <sys>
using namespace std;

bool unique(string s){
    map<char,int> map2;
    for(auto key: s){
        if(map2.count(key)==0){
            map2[key] = 0;
        }
        map2[key] ++;
        if (map2[key]==2){
            return false;
        }
    }
    return true;
}
int max_length(string s){
    size_t size = s.size();
    for(int i=size;i>=1;i--){
        for(int j=0;j<size-i+1;j++){
            string substr = s.substr(j,i);
            if(unique(substr)){
                return i;
            }
        }
    }
    return 0;
}
int main(int argc, char** argv){
    string s = "rzzohjzqefpmhugxxhtvmwzxuzcfzsertghbpittnjiudorbxmwkjvjfxnmwfrpzxwametiresniiglgtjsegd";    
    int x = max_length(s);
    // cout << x << endl;
    
    
    return EXIT_SUCCESS;
}
