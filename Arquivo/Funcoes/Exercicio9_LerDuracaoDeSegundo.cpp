//
// 29/09/2024.
//
#include <stdio.h>
int main(){

    int duracaoDeSegundo;

    printf("digite o total de segundo: ");
    scanf("%d",&duracaoDeSegundo);

    int hora = duracaoDeSegundo / 3600;
    int minuto = (duracaoDeSegundo % 3600) / 60;
    int segundo = duracaoDeSegundo % 60;

    printf("quantidade de tempo é: %d:%02d:%02d \n",hora,minuto,segundo);

    return 0;
}
