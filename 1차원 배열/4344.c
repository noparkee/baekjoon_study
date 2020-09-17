#include <stdio.h>
#include <stdlib.h>
int main(){
	int c, num;
	int sum = 0;
	float avg = 0;
	int st = 0;
	
	scanf("%d", &c);
	int **a = malloc(sizeof(int*) * c);
	/*for (int i = 0; i<c; i++)
		a[i] = malloc(sizeof(int) * 1000);*/
	
	for (int i = 0; i<c; i++){
		scanf("%d", &num);
		a[i] = malloc(sizeof(int) * (num+1));
		a[i][0] = num;
		for (int j = 1; j<(num+1); j++)
			scanf("%d", &a[i][j]);
	}
	
	for ( int i = 0; i<c; i++){
		for (int j = 1; j<a[i][0]+1; j++){
			sum += a[i][j];
		}
		avg = sum / a[i][0];
		for (int j = 1; j<a[i][0]+1; j++){
			if (avg < a[i][j])
				st++;
		}
		printf("%.3f%%\n", (float)st/a[i][0] * 100);
		sum = 0;
		avg = 0;
		st= 0;
	}
	
	for (int i = 0; i<c; i++)
		free(a[i]);
	free(a);
	
	return 0;
}
