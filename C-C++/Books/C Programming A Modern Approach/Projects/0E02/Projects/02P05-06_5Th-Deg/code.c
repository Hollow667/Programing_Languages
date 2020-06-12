#include <stdio.h>

int main()
{
  float x;
  printf("enter x: ");
  scanf("%f", &x);
  printf("%f", 3*x*x*x*x*x + 2 *x*x*x*x - 5*x*x*x - x*x + 7*x - 6);
  // Horner's Rule
  printf("\n%f", ((((3*x+2)*x - 5)*x-1)*x+7)*x-6);
  return 0;
}