#include <stdio.h>
#include <stdlib.h> 
int main(){
	    int a, temp;
	        
	        scanf("%d", &a);
		    int* arr = malloc(sizeof(int) * a);
		        
		        for(int i = 0; i<a; i++){
				        scanf("%d", &arr[i]);
					    }
			    
			    for (int i = 0; i<a-1; i++){
				            for (int j = i+1; j<a; j++){
						                if (arr[i] > arr[j]){
									                temp = arr[i];
											                arr[i] = arr[j];
													                arr[j] = temp;
															            }
								        }
					        }
			        
			        for (int i = 0; i<a; i++)
					        printf("%d\n", arr[i]);
				    
				    return 0;
}
