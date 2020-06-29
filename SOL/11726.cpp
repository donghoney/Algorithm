#include <iostream>
using namespace std;

int tile(int a){
    if(a == 2) return 2;
    else{
        return tile(a-1)+tile(a-2);
    }
}

int main(){
    
    int size, b;

    cin >> size;

    cout << tile(size);

}