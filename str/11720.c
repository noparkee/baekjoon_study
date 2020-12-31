#include <stdio.h>
int main(){
	int a;
	char b[100];
	long long sum = 0;
	scanf("%d", &a);
	scanf("%s", b);
	for (int i = 0; i<a; i++){
		sum += b[i] - 48;
	}
	printf("%lld", sum);

	return 0;
}
