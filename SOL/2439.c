#include <stdio.h>

int main(void) {
	int a;
	
	scanf("%d",&a);
	
	for(int i=0; i<a; i++){
		int k=i+1;
		int j=a-k;
		
		for(; j>0; j--){
			printf(" ");
		}
		for(k; k>0; k--){
			printf("*");
		}
		printf("\n");
	}
	
	return 0;
}
