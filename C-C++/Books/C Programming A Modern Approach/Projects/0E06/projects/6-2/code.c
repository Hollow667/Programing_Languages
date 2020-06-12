#include <stdio.h>
// GCD
int min(int num1, int num2){return num1 <= num2 ? num1 : num2;}
int GCD(int num1, int num2)
{
  int i = min(num1, num2);
  while(!((num1 % i == 0) && (num2 % i == 0))){i = i - 1;}
  return i;
}
 
int main(void)
{
  int num1, num2;
 
  printf("Enter two integers: ");
  scanf("%i %i", &num1, &num2);
  printf("Greatest common divisor: %i", GCD(num1, num2));
  return 0;
}