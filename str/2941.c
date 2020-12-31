#include <stdio.h>
#include <string.h>
int main(){
	char c[101];
	char pat[8][4] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
	int  len, a;
	char *p;
	scanf("%s", c);
	len = strlen(c);

	for (int i = 0; i<8; i++){
		p = strstr(c, pat[i]);
		a = strlen(pat[i]);
		while(p != NULL){
			len -= 1;
			p = strstr(p + a, pat[i]);
		}
	}

	printf("%d\n", len);
	return 0;
}
