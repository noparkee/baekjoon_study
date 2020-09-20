#include <stdio.h>
#include <string.h>
int main(){
	char c[16] = {0};
	int sum = 0, n, m;
	scanf("%s", c);
	int len = strlen(c);
	
	for(int i = 0; i<len; i++){
		n = (c[i]-65)/3;
		if (n <=5){
			sum = sum+ n+3;
		}
		
		else if(n == 6 || n == 7){
			m = (c[i]-65)%3;
			if(m==0){
				sum = sum+ n+2;	
			}
			else{
				sum = sum+ n+3;
			}
		}
		else
			sum += 10;
	}

	printf("%d", sum);

	return 0;
}
