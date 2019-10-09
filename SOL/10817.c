#include <stdio.h>

int main(void) {
	
	int a, b, c;
	int a1 = 0, b1 = 0, c1 = 0;
	scanf("%d %d %d", &a, &b, &c);
	
	if(a > b){
		a1++;
		b1--;
		if(a > c){
			a1++;
			c1--;
			if(b > c){
				b1++;
				c1--;
			}
			else{
				c1++;
				b1--;
			}
		}
		else{
			a1--;
			c1++;
		}
	}
	else if(b > c){
		b1+=2;
		a1--;
		c1--;
		if(a > c){
			a1++;
			c1--;
		}
		else{
			a1--;
			c1++;
		}
	}
	else{
		if(a > b){
			b1--;
		}
		else{
			a1--;
		}
	}
	
	if(a1 == 0){
		printf("%d", a);
	}
	else if(b1==0){
		printf("%d", b);
	}
	else{
		printf("%d", c);
	}
	
	return 0;
}
