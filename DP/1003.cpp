nclude <iostream>
#include <vector>
using namespace std;

int main(){
    int fib[2][41];
    int input, n;
    vector<int> v; 
    
    fib[0][0]=1;
    fib[0][1]=0;
    fib[1][0]=0;
    fib[1][1]=1;
    for(int i=2; i<41; i++){
        fib[0][i]=fib[0][i-1]+fib[0][i-2];
        fib[1][i]=fib[1][i-1]+fib[1][i-2];
    }
    
    cin >> input;
    for(int i=0; i<input; i++){
        cin >> n;
        v.push_back(n);
    }
    
    for(int i=0; i<input; i++){
        cout << fib[0][v[i]] << " " << fib[1][v[i]] << '\n';
    }
    
    return 0;
}
