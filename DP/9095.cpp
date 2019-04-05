#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    int arr[12];
    arr[0]=0;
    int input[10000];
    int T=0;
    
    for(int i=1; i<11; i++){
        if(i==1) arr[1]=arr[0]+1;
        else if(1<i&&i<4) arr[i]=arr[i-1]*2;
        else {
            arr[i]=arr[i-1]+arr[i-2]+arr[i-3];
        }
    }
    
    scanf("%d",&T);
    for(int i=0; i<T; i++){
        scanf("%d",&input[i]);
    }
    for(int i=0; i<T; i++){
        printf("%d\n", arr[input[i]]);
    }
    return 0;
}
