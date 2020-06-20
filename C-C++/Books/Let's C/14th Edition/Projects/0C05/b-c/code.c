#include <stdio.h>
#include <math.h>

int main(void)
{
  float n1, n2;
  printf("Enter two numbers: ");
  scanf("%f,%f", &n1, &n2);
  printf("%.f^%.f = %.f", n1, n2, pow(n1, n2));

  return 0;
}