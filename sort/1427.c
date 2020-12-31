#include <stdio.h>
#include <stdlib.h>

int main(){
    int a, tmp;
    int n[10] = {0}; 
    
    scanf("%d", &a);
    while (a > 0){
        tmp = a % 10;
        n[tmp] ++;
        a /= 10;
    }

    for (int i = 9; i >= 0; i--){
        if (n[i] != 0){
            for (int j = 0; j<n[i]; j++)
                printf("%d", i);
        }
    }
    
    return 0;
}