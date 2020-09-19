#include <stdio.h>
int main(){
	int a, b;
	char c[20];
	scanf("%d", &a);
	
	for(int i = 0; i<a; i++){
		scanf("%d %s", &b, c);
		for (int j = 0; c[j] != 0; j++){
			for(int k = 0; k<b; k++)
				printf("%c", c[j]);
		}
		printf("\n");
		for(int j = 0; j<20; j++)
			c[j] = 0;
	}

	return 0;
}
