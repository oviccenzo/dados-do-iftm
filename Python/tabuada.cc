#include <stdio.h>

int main(){

    int numero,i;

    printf("Digite um numero: ");
    scanf("%d" , &numero);

    printf("Tabuada de %d: \n",numero); 
    
    for(i = 1; i <= 10; i++){

        printf("%d x %d = %d\n",numero, i, i*numero);
    }

    return 0;
}
