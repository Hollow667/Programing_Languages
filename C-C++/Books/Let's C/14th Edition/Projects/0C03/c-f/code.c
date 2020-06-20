#include <stdio.h>

int main(void)
{
  float deg=0; float sum = 0;
  do
  {
    sum += deg;
    printf("Enter degree: ");
    scanf("%f", &deg);
  }while(deg >= 0);

  printf("The sum is: %.lf", sum);
  return 0;
}