#include <stdio.h>

int main(void) {
	int arr[1000000];
    int input;
    
    scanf("%d",&input);
  
    arr[0]=0;
    arr[1]=1;
    arr[2]=1;
    for(int i=4; i<=input; i++){
        int min=0;
        if(i%2==0) min=arr[(i/2)-1];
        if(i%3==0){
            if(min==0||min>arr[(i/3)-1]) min=arr[(i/3)-1];
        }
        if(min==0||min>arr[i-2]) min=arr[i-2];
        
        arr[i-1]=min+1;
    }
    
    printf("%d\n", arr[input-1]);
    return 0;
}
