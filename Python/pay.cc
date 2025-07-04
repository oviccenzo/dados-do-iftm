//18/11/2023
//Calcular o numero par nao divisivel por a ou 2
#include <cstdio>
int EPar(int a){
    if(a%2)      /* Verifica se a divisivel por dois */
        return 0;
    else
        return 1;
}
int main(){
    int num;
    printf("Entre com numero: ");
    scanf("%d",&num);
    if(EPar(num))
        printf("\n\nO numero e par.\n");
    else
        printf("\n\nO numero e impar.\n");
    return 0;
}