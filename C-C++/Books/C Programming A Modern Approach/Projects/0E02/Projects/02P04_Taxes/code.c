#include <stdio.h>

int main()
{
  float dollars_and_cents;
  printf("Enter an amount: ");
  scanf("%f", &dollars_and_cents);
  printf("With tax added: $%.2f", 1.05 * dollars_and_cents);
  return 0;
}