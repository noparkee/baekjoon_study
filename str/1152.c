#include <stdio.h>
#include <string.h>
// 공백을 포함한 문자열은 scanf로 x, 이 문제에서 문자열 끝에 공백이 여러개 있는경우 strtok로 하면 +1 의 결과가 나오기 때문에 strtok를 쓸거면 문자열 끝의 공백을 다 지워줘야하는 듯

int main(){
	char s[1000001];
	int cnt = 0, len;
	char* ptr;
	
	fgets(s, sizeof(s), stdin);
	len = strlen(s);
	
	for (int i = len-1; s[i] == 32 || s[i] == 10; i--)
		s[i] = 0;


	ptr = strtok(s, " ");
	while(ptr != NULL){
		cnt ++;
		ptr = strtok(NULL, " ");
	}

	printf("%d", cnt);
	return 0;
}
