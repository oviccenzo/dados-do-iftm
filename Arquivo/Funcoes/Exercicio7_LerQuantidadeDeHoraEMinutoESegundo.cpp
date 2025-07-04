//
//29/9/2024 as 6h20 da noite
//
#include <stdio.h>
int main(){

    int hora,minuto,segundo;

    printf("digite a quantidade de hora: ");
    scanf("%d",&hora);

    printf("digite a quantidade de minuto: ");
    scanf("%d",&minuto);

    printf("digite a quantidade de segundo: ");
    scanf("%d",&segundo);

    int totalDeSegundo = (hora * 3600)  + (minuto * 60) + segundo;

    printf("o total de segundo e: %d",totalDeSegundo);
}