#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// strlen을 for문 안에 넣으면, for문을 돌 때마다 strlen을 계산하기 때문에 시간초과

int main(){
	char s[1000000];
	int a[26] = {0, };
	int max = 0;
	int cnt, maxindex;
	int len;
	scanf("%s", s);
	len = strlen(s);
	for(int i = 0; i<len; i++){
		if( s[i] >= 65 && s[i] <=90){ 	//대문자
			a[s[i]-65]++;
		}
		if(s[i] >= 97 && s[i] <= 122)
			a[s[i]-97]++;
	}
	

	cnt = 0;
	for(int i = 0; i<26; i++){
		if (max < a[i]){
			cnt = 0;
			max = a[i];
			maxindex = i;
		}
		else if (max == a[i])
			cnt++;
	}
	
	if (cnt ==0)
		printf("%c", maxindex+65);
	else
		printf("?");
	

	return 0;
}
