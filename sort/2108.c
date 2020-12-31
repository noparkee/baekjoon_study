#include <stdlib.h>
#include <stdio.h>

int compare(const void *a, const void *b){
	int num1 = *(int *)a;
	int num2 = *(int *)b;
	if (num1 < num2)
		return 1;
	if (num1 > num2)
		return -1;
	return 0;
}

int main(){
	int num;
	int sum = 0;
	int o[4];
	int f[8001] = {0};

	scanf("%d", &num);

	int a[num];
	for (int i = 0; i<num; i++){
		scanf("%d", &a[i]);
		sum += a[i];

		f[a[i] + 4000] ++;
	}
	
	if (sum < 0)
		o[0] = (int)((float)sum/num - 0.5f);
	else
		o[0] = (int)((float)sum/num + 0.5f);

	qsort(a, num, sizeof(int), compare);
	
	o[1] = a[(num+1)/2 - 1];
	int max_fre = 0;
	int cnt = 0;
	int t;
	for (int i = 0; i<8001; i++){
		if (max_fre < f[i])
			max_fre = f[i];		
	}
	for (int i = 0; i<8001; i++){
		if (max_fre == f[i]){
			cnt ++;
			t = i - 4000;
		}
		if (cnt == 2){
			o[2] = t;
			break;
		}
	}

	if (cnt == 1)
		o[2] = t;

	o[3] = a[0] - a[num-1];

	for (int i = 0; i<4; i++)
		printf("%d\n", o[i]);
	
	return 0;
}
