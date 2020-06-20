#include <stdio.h>
int main(void)
{
  float c, d;
  printf("Enter two numbers: ");
  scanf("%f %f", &c, &d);
  c+=d;d=c-d;c=c-d;
  printf("Numbers are: %.lf %.lf", c , d); 
  return 0;
}