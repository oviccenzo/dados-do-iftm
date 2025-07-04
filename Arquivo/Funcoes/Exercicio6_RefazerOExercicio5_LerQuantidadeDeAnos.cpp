//
// 29/9/2024 as 6h da noite
//
#include <stdio.h>

float f_amd_dias(int dias, int meses, int anos){

    return ((anos * 365) + (meses * 31) + anos);
}

int main(){

    int dias, meses, anos;

    printf("digite o dia: ");
    scanf("%d",&dias);

    printf("digite o meses: ");
    scanf("%d",&meses);

    printf("digite o anos: ");
    scanf("%d",&anos);

    int totalDoDias = f_amd_dias(dias,meses,anos);

    printf("o total do dia e:  %d dias",totalDoDias);
}