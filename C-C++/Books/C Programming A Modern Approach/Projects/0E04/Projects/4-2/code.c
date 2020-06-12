#include <stdio.h>
int main(void)
{
  int num; char n[4];

  // first way
  printf("Enter a two-digit number: ");
  scanf("%i", &num);
  printf("The reversal is: %i%i%i\n",num - num / 10 * 10,(num - num / 100 * 100) / 10,  num /100);

  // second way
  printf("Enter a two-digit number: ");
  scanf("%s", &n);
  printf("The reversal is: %c%c%c", n[2], n[1], n[0]);

  return 0;
}