#include <cstdio>

float nota1, nota2,nota3,media;

void le_nota(){
    printf("digite a primeira nota: \n");
    scanf("%f",&nota1);
    printf("digite a segunda nota: \n");
    scanf("%f",&nota2);
    printf("digite a terceira nota: \n");
    scanf("%f",&nota3);
}

void f_media(){

    media = (nota1 * 2 + nota2 * 3 + nota3 * 4) / 9;
}

void imprimi(){

    printf("o resultado da tres prova e: %.2f",media);
}

int main(){

    le_nota();
    f_media();
    imprimi();
}