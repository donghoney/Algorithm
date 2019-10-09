#include <stdio.h>

int main(void) {
	
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);
	
	int one, ten, hun;
	one = a * (b%10);
	ten = a * ((b%100 - b%10)/10);
	hun = a * (b/100);
	
	printf("%d\n", one);
	printf("%d\n", ten);
	printf("%d\n", hun);
	printf("%d\n", a*b);
	
	return 0;
}
