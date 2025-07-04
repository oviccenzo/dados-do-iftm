//
// Created by Robert L Resende on 29/09/24.
//

#include <stdio.h>

int main(){

    int anos,meses,dias;

    printf("calcular a quantidade de anos: ");
    scanf("%d",&anos);

    printf("calcular a quantidade de meses: ");
    scanf("%d",&meses);

    printf("calcular a quantidade de dias: ");
    scanf("%d",&dias);

    int somaDosDias = (anos * 365) + (meses * 31) + anos;

    printf("soma da quantidade de anos e meses e anos e: %d dias", somaDosDias);
}