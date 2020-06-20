#include <stdio.h>

int main(void)
{
  int num, sum;sum = 0;
  printf("Enter number: ");
  scanf("%i", &num);
  while((10 * (num / 10) - num) != 0)
  {
    sum +=  (num - 10 * (num / 10));sum *= 10;
    num = num / 10;
  }
  sum = sum / 10;
  printf("The number in reverse digits is: %i", sum);
  return 0;
}