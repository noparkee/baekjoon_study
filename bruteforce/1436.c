#include <stdio.h>

int main(){
    int n, d;
    int temp = 0;
    int cnt = 1;
    int num = 1666;
    scanf("%d", &n);

    if (n==1)
        printf("666");
    else{
        while (1){
            d = num;
            while (d > 0){
                if (d%10 == 6)
                    temp ++;
                else
                    temp=0;
                
                if (temp == 3)
                    break;

                d = d / 10;
            }
            
            if (temp == 3){
                cnt++;
                if (cnt == n){
                    printf("%d", num);
                    break;
                }
            }

            num++;
            temp=0;
        }
    }
    return 0;
}