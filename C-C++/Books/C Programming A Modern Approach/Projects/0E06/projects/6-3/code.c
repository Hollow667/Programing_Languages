#include <stdio.h>

int min(int num1, int num2){return num1 <= num2 ? num1 : num2;}
int GCD(int num1, int num2){int i = min(num1, num2);while(!((num1 % i == 0) && (num2 % i == 0))){i = i - 1;}return i;}
 
int main(void)
{
  int num1, num2;
  printf("Enter a fraction: ");
  scanf("%i/%i", &num1, &num2);
  printf("In lowest terms: %i/%i", num1/GCD(num1, num2), num2/GCD(num1, num2)); 
  return 0;
}