//
// 29/08/2024
//
#include <stdio.h>

int f_amd_seg(int horas, int minutos, int segundos){
    return ((horas * 3600) + (minutos * 60) + segundos);
}

int main(){

    int hora,minuto,segundo;

    printf("digite a quantidade de hora: ");
    scanf("%d",&hora);

    printf("digite a quantidade de minuto: ");
    scanf("%d",&minuto);

    printf("digite a quantidade de segundo: ");
    scanf("%d",&segundo);

    int totalDeSegundo = f_amd_seg(hora,minuto,segundo);

    printf("o total de segundo e: %d\n", totalDeSegundo);
}