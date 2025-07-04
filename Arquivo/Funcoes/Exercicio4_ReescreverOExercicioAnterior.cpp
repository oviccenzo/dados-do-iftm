//
// Created by Robert L Resende on 29/09/24.
//
#include <cstdio>
#define PI 3.1459

//declarando void como variavel global
float f_area(float raio) {
    return raio = PI * raio * raio;
}

float f_peri(float raio){
    return raio = 2 * PI * raio;
}

int main(){

    float peri,area,raio;

    //digitando o valor do raio da circuferencia
    printf("calcular o raio: ");
    scanf("%f",&raio);

    //calculando o raio da area e do raio do perimetro
    area = f_area(raio);
    peri = f_peri(raio);

    printf("o calculo da area do raio da circuferencia: %.2f\n",area);
    printf("o calculo do perimetro do raio da circuferencia: %.2f\n",peri);

    //return 0;
}