#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
int main(){
	    int a;
	    int cnt = 1;
		int sum = 0;
		scanf("%d", &a);
		char **b = malloc(sizeof(char*) * a);
		for (int i = 0; i<a; i++)
			b[i] = malloc(sizeof(char) * 80);
				        
		for (int i = 0; i<a; i++){
		    scanf("%s", b[i]);
		}
				        
		for (int i = 0; i<a; i++){
		    cnt = 1;
		    if (b[i][0] == 'O')
				sum += cnt;
			for (int j = 1; j<strlen(b[i]); j++){
				if (b[i][j] == 'O' && b[i][j-1] == 'O'){
				    cnt ++;
				    sum += cnt;
				}
				else if (b[i][j] == 'O' && b[i][j-1] == 'X'){
				    cnt = 1;
				    sum += cnt;
				}
			}
			printf("%d\n", sum);
			sum = 0;
		}
		for (int i = 0; i<a; i++){
			free(b[i]);
		}
		free(b);
						      
		return 0;
}
