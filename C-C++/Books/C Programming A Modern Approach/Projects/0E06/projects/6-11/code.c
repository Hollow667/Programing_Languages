#include <stdio.h>

float p(int n){float res = 1; float i = 1;while(i <= n){res = res * i;i++;} return res;}

float e(){int n = 10 ; int i = 1 ; float res = 1 ; while( i <= n ){res += 1.0 / (1.0 * p(i)); i++;}return res;}

int main(void){printf("%f",   e());return 0;}