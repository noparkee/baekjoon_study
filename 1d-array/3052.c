#include <stdio.h>
int main(){
    int a[10];
    int b, k;
    int cnt=1;
    
    for (int i=0; i<10; i++){
        k = 0;
        scanf("%d", &b);
        a[i] = b%42;
        if (i != 0){
            for (int j = 0; j<i; j++){
                if(a[j] != a[i])
                    k++;
            }
            if (k == i)
                cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}