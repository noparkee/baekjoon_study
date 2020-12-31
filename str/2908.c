#include <stdio.h>
#include <stdlib.h>
int main(){
	char a[4], b[4];
	int k;
	int m,n ;
	scanf("%s %s", a, b);
	k = a[0];
	a[0] = a[2];
	a[2] = k;

	k = b[0];
	b[0] = b[2];
	b[2] = k;
		

	m = atoi(a);
	n = atoi(b);
	if (m>n)
		printf("%d",m);
	else
		printf("%d", n);

	return 0;
}
