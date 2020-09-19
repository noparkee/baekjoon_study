#include <stdio.h>
int main(){
	int a[26];
	char s[100];
	scanf("%s", s);
	
	for (int i = 0; i<26; i++)
		a[i] = -1;

	for (int i = 0; s[i]!= 0; i++){
		if(a[s[i]-97] == -1)
			a[s[i]-97] = i;

	}

	for (int i = 0; i<26; i++)
		printf("%d ", a[i]);

	return 0;
}
