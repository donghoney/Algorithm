#include <stdio.h>

int main(void) {

       int n;
       long long fib[91];
       scanf("%d", &n);
       
       for(int i=0; i<=n; i++){
       	if(i==0) fib[i] = 0;
       	else if(i==1) fib[i] = 1;
       	else if(i>=2){
       		fib[i] = fib[i-1]+fib[i-2];
       	}
       }
       
       printf("%lld", fib[n]);
       
       return 0;
}
