#include <stdio.h>
int min(int a, int b);

void numSwap(int a, int b);

void numSwap2(int c, int d);

int main(){
	int x = 10;
	int y = 5;
	//numSwap2(x, y);
	int temp;
	temp = x;
	x = y;
	y = temp;
	printf("After swap: x = %d and y = %d\n", x, y);
	return 0;
}

void numSwap(int a, int b){
	a = a + b;
	b = a - b;
	a = a - b;
	return;
}

void numSwap2(int c, int d){
	int temp;
	temp = c;
	c = d;
	d = temp;
	return;
}

int min(int a, int b){
	int final;
	if(a < b){
		final = a;
	}
	else{
		final = b;
	}
	return final;
}