#include <iostream>
using namespace std;

int max(int a, int b){
	return a>b?a:b;
}

int main() {
	int arr[300];
	int input[300];
	int num;
	
	cin >> num;
	for(int i=0; i<num; i++){
		cin >> input[i];
	}
	
	arr[0]=input[0];
	arr[1]=input[0]+input[1];
	for(int i=2; i<num; i++){
		if(i<3) arr[i]=max(input[i]+input[i-1], input[i]+input[i-2]);
		else arr[i]=max(input[i]+input[i-1]+arr[i-3], input[i]+arr[i-2]);
	}
	
	cout << arr[num-1];
	return 0;
}
