#include <stdio.h>

int main(){
    int a, max;
    double sum = 0;
    scanf("%d", &a);
    int s[a];
    for (int i = 0; i<a; i++){
        scanf("%d", &s[i]);
        sum += s[i];
    }
    max = s[0];
    for (int i=1; i<a; i++){
        if(max < s[i])
            max = s[i];
    }
    printf("%lf", sum/a * 100/max);
    return 0;
}