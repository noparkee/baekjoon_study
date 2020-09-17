#include <stdio.h>

int main(){
    int a, b, c, k;
    long long d;
    int num[10] = {0, };
    
    scanf("%d %d %d", &a, &b, &c);
    d = a*b*c;
    
    while(d>0){
        k = d%10;
        num[k] ++;
        d = d/10;
    }
    
    for (int i =0 ;i<10; i++){
        printf("%d\n", num[i]);
    }
    return 0;
}