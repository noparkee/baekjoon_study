#include <stdio.h>

int main(){
	int a;
	int temp;
	scanf("%d", &a);

	int b[10001] = { 0 };
	for(int i = 0; i<a; i++){
		scanf("%d", &temp);
		b[temp]++;
	}

	for (int i = 0; i<10001; i++){
		if (b[i] != 0){
			for (int j = 0; j<b[i]; j++){
				printf("%d\n", i);
			}
		}
	}

	return 0;
}
