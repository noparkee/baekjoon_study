#include <stdio.h>
#include <stdlib.h>

int compare(const void *first, const void* second){
	if (*(int*)first > *(int*)second)
		return 1;
	else if (*(int*)first < *(int*)second)
		return -1;
	else
	        return 0;
}

int main(){
	int a;
	scanf("%d", &a);
	int *arr = malloc(sizeof(int) * a);
	for (int i = 0; i<a; i++)
		scanf("%d", &arr[i]);
		    
	qsort(arr, a, sizeof(int), compare);
			        
	for (int i = 0; i<a; i++)
        printf("%d\n", arr[i]);
		    
	return 0;
}
