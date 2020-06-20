#include <stdio.h>
// there is a small error in the series ln(i) = Simga(n=1->...) (1/n)((i-1)/i)^n
#include <math.h>

float Log(float n){
float res = 0;int i = 0;
res = res + 1.0* (n - 1) / n;
for(i = 2; i < 100; i++){ res += (1.0 / i) * pow((1.0*(1.0 * n-1.0)/n), i);}
return res;
}

int main(void){
float n;
printf("Enter number to calculate its natural logarithm: ");
scanf("%f", &n);
printf("ln(%f) = %f",n, Log(n));
return 0;
}