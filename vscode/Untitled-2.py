# #include <stdio.h>
#
# // Função para calcular a potência
# double potencia(double base, int expoente) {
#     double resultado = 1.0;
#     for (int i = 0; i < expoente; i++) {
#         resultado *= base;
#     }
#     return resultado;
# }
#
# int main() {
#     double base;
#     int expoente;
#
#     // Pedir os valores ao usuário
#     printf("Digite a base: ");
#     scanf("%lf", &base);
#     printf("Digite o expoente: ");
#     scanf("%d", &expoente);
#
#     // Verificar se o expoente é válido
#     if (expoente < 0) {
#         printf("Erro: Expoente deve ser maior ou igual a zero.\n");
#         return 1;
#     }
#
#     // Calcular e imprimir o resultado
#     double resultado = potencia(base, expoente);
#     printf("%.2f elevado a %d é igual a %.2f\n", base, expoente, resultado);
#
#     return 0;
# }
