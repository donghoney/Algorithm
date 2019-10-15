#include <stdio.h>

int main(void) {

        int n, min;
        scanf("%d %d", &n, &min);
        
        int *list = malloc(sizeof(int)*n);
        
        for(int i=0; i<n; i++){
        	int a;
        	scanf("%d", &a);
        	list[i] = a;
        }
        
        for(int i=0; i<n; i++){
        	if(list[i] < min) printf("%d ", list[i]);
        }
        return 0;
}
