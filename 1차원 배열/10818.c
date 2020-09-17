#include <stdio.h>
int main(){
    int n;
    int max, min;
    scanf("%d", &n);
    
    int a[n];
    for(int i = 0; i<n;i++){
        scanf("%d", &a[i]);
        if(i==0){
            max = a[i];
            min = a[i];
        }
        else{
            if (max < a[i])
                max = a[i];
            if (min > a[i])
                min = a[i];
        }
    }
    printf("%d %d", min, max);
    return 0;
}