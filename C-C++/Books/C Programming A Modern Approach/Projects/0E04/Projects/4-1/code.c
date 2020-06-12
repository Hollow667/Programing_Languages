#include <stdio.h>
int main(void)
{
  int num; char n[3];

  // first way
  printf("Enter a two-digit number: ");
  scanf("%i", &num);
  printf("The reversal is: %i%i\n", num - num / 10 * 10, num / 10);

  // second way
  printf("Enter a two-digit number: ");
  scanf("%s", &n);
  printf("The reversal is: %c%c", n[1], n[0]);

  return 0;
}