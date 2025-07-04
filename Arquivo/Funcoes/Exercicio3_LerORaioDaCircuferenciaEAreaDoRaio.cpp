//
// Created by Robert L Resende on 28/09/24 e 29/09/2024.
//
#include <stdio.h>
#define PI 3.1415


float raio,area,peri;

void f_leitura(){

    printf("digite o raio: ");
    scanf("%f",&raio);
}

float f_area(float d) {
    area = PI * raio * raio;
}

void f_peri(){
    peri = 2 * PI * raio;
}

void f_imprimi(){

    f_leitura();
    f_area(0);
    f_peri();

    printf("a area do circulo e: %.2f\n",area);
    printf("o perimetro do circulp e: %.2f\n",peri);
}

int main(){

    f_imprimi();
    return 0;
}
