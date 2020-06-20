#include <stdio.h>

int main(void)
{
  int num, sum;sum = 0;
  printf("Enter number: ");
  scanf("%i", &num);
  while((10 * (num / 10) - num) != 0)
  {
    sum += num - 10 * (num / 10);
    num = num / 10;
  }
  printf("The sum of the number digits is: %i", sum);
  return 0;
}