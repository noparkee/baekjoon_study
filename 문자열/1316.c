#include <stdio.h>
#include <string.h>
int main(){
	int n, len, cnt, num;
	char c[101];
	int a[26] = {0, };
	scanf("%d", &n);
	num = n;
	for(int i = 0; i<n; i++){	// 몇 개의 단어
		scanf("%s", c);
		len = strlen(c);
		a[c[0]-97] ++;
			
		for (int j = 1; j<len; j++){	// 하나의 단어 안에서
			if(c[j] == c[j-1])
				a[c[j]-97]++;
			else{
				if(a[c[j]-97] != 0){
					num--;
					break;
				}
				else
					a[c[j]-97] ++;
			}
		}

		for(int k = 0; k<26; k++)
			a[k] = 0;
	}
	printf("%d", num);

	return 0;
}
