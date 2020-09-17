#include <stdio.h>
int main(){
    int a, b, max;
    for (int i = 0; i<9; i++){
        scanf("%d", &a);
        if (i == 0){
            max = a;
            b = i+1;
        }
        else{
            if(max < a){
                max = a;
                b = i+1;
            }
        }
    }
    printf("%d\n%d", max, b);
    return 0;
}